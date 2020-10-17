from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mass_mail
from maniva_webapp.forms import ContactForm

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
            location = g.city(get_client_loc(request))
            form.cleaned_data['country'] = location
            form.save()
            send_email(request)
            push_notifications(request)
            form = forms.ContactForm()
    args = {'form':form}
    return render(request, self.template_name, args)

def get_client_loc(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    location = g.city(ip)
    return loc

def send_email(request):
    send_mass_mail("Hello from Maniva Digital", 
    "Let's get started with your digital transformation!", 
    'werdperk@outlook.com', 
    ['toleyo1560@ofdyn.com'],
    fail_silently=False)
    return render(request, self.template_name)

def push_notifications(request):
    pass