from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.gis.geoip2 import GeoIP2 as g
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mass_mail
from maniva_webapp.forms import ContactForm

## HOMEPAGE TEMPLATE
class HomePageView(TemplateView):
    template_name='index.html'

## FORMS 
# HTTP Methods
def get(request):
    form = ContactForm()
    args = {'form':form}
    return render(request, self.template_name, args)

def post(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        send_email(request)
        push_notifications(request)
        form = forms.ContactForm()
        return redirect('index')
    args = {'form':form}
    return render(request, self.template_name, args)

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        send_mass_mail(subject, message, from_email, ['werdperk@outlook.com'])
        return redirect('index')

def push_notifications(request):
    pass

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip