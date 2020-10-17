from django import forms
from django.forms import ModelForm
from maniva_webapp.models import Contact, Consultation

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        model.country = g.
        fields = ['name','email','subject','message']

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = 'name','email','subject','message']