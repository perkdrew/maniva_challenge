import pymongo
import os

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms, views, models

user = os.environ.get('myUserAdmin')
password = os.environ.get('abc123')
client = pymongo.MongoClient(f'mongodb+srv://{user}:{password}@cluster0-ysglw.mongodb.net/')

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
            form = forms.ContactForm()
            return redirect("index")
    args = {'form':form}
    return render(request, self.template_name, args)



