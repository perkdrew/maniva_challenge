from django import forms
from django.forms import ModelForm
from maniva_webapp.models import Contact, Consultation

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject','message','country']

    def update_country_field(self, field, update):
        if field == 'country':
            Contact.country = str(update)
        return Contact.country

    def get_email(self):
        return Contact.email

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['title','description','client_name']