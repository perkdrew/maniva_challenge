from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from maniva_crm.models import *
from maniva_crm.forms import ServiceForm, CreateUserForm
from maniva_crm.filters import ServiceFilter
from maniva_crm.decorators import unauthenticated_user, allowed_users, admin_only


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            group = Group.objects.get(name="customer")
            user.groups.add(group)
            messages.success(request, "Account was created for " + username)
            return redirect("login")
    context = {"form": form}
    return render(request, "register.html", context)


@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username OR password is incorrect")
    context = {}
    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
@admin_only
def home(request):
    services = Service.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = services.count()
    delivered = services.filter(status="Delivered").count()
    pending = services.filter(status="Pending").count()
    context = {
        "services": services,
        "customers": customers,
        "total_orders": total_orders,
        "delivered": delivered,
        "pending": pending,
    }
    return render(request, "dashboard.html", context)


def userPage(request):
    context = {}
    return render(request, "user.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def services(request):
    services = Service.objects.all()

    return render(request, "services.html", {"services": services})


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    services = customer.service_set.all()
    service_count = services.count()
    myFilter = ServiceFilter(request.GET, queryset=services)
    serivces = myFilter.qs
    context = {
        "customer": customer,
        "services": services,
        "service_count": service_count,
        "myFilter": myFilter,
    }
    return render(request, "customer.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def createServiceOrder(request, pk):
    ServiceFormSet = inlineformset_factory(
        Customer, Service, fields=("service", "status"), extra=10
    )
    customer = Customer.objects.get(id=pk)
    formset = ServiceFormSet(queryset=Service.objects.none(), instance=customer)
    if request.method == "POST":
        form = ServiceForm(request.POST)
        formset = ServiceFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect("/")
    context = {"form": formset}
    return render(request, "service_form.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def updateServiceOrder(request, pk):
    service = Service.objects.get(id=pk)
    form = ServiceForm(instance=service)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "service_form.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def deleteServiceOrder(request, pk):
    service = Service.objects.get(id=pk)
    if request.method == "POST":
        service.delete()
        return redirect("/")

    context = {"service": service}
    return render(request, "delete.html", context)
