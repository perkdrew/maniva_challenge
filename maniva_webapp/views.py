from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
#from django.contrib.gis.geoip2 import GeoIP2
from django.core.mail import send_mail
from maniva_webapp.forms import ContactForm

#g = GeoIP2()

## HOMEPAGE TEMPLATE
class HomePageView(TemplateView):
    template_name='index.html'

## Site functions
def manage_contacts(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            ip = get_client_ip(request)
            # need specific files for geolocations
            #location = g.country(str(ip))
            form.update_country_field('country', ip)
            form.save()
            curr_email = form.get_email()
            send_email(request, curr_email)
            push_notifications(request)
            form = ContactForm()
    args = {'form':form}
    return render(request, self.template_name, args)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def send_email(request, curr_email):
    send_mail("Hello from Maniva Digital", 
    "Let's get started with your digital transformation!", 
    'werdperk@outlook.com', 
    [curr_email],
    fail_silently=False)
    return render(request, self.template_name)

def push_notifications(request):
    pass