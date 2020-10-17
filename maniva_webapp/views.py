from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from maniva_webapp.forms import ContactForm

#from django.contrib.gis.geoip2 import GeoIP2
#g = GeoIP2()


## HOMEPAGE TEMPLATE
class HomePageView(TemplateView):
    template_name='index.html'


# Site functions
def manage_contacts(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            ip = get_client_ip(request)
            form.save()
            send_email(request)
            push_notifications(request)
            form = ContactForm()
    return render(request, self.template_name, {'form':form})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def send_email(request):
    form = ContactForm()
    send_mail("Hello from Maniva Digital", 
    "Let's get started with your digital transformation!", 
    'werdperk@outlook.com', 
    [form],
    fail_silently=False)
    return render(request, self.template_name, {'form':form})

def push_notifications(request):
    pass