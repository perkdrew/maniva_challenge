from django import forms
from django.forms import ModelForm
from .models import Contact, Consultation

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = '__all__'