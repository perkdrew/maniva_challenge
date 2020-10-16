from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mass_mail
from . import forms, views, models

## HOMEPAGE TEMPLATE
class HomePageView(TemplateView):
    template_name='index.html'

## FORMS 
# HTTP Methods
def get(request):
    form = forms.ContactForm()
    args = {'form':form}
    return render(request, self.template_name, args)

def post(request):
    if request.method == 'POST':
        print(request.POST)
        form = forms.ContactForm(request.POST)
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



