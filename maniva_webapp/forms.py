from django import forms
from django.forms import ModelForm
from maniva_webapp.models import Contact, Consultation

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject','message','country']

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['title','description','client_name']