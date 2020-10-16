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
    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            gen_mail = ('Thanks for reaching out!', 
                        'We appreciate you contacting us and hope to make your digital transfer as smoothly as possible.',
                        [form['email']])
            send_mass_mail((gen_mail), fail_silently=False)
            form = forms.ContactForm()
            return redirect("index")
    args = {'form':form}
    return render(request, self.template_name, args)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip