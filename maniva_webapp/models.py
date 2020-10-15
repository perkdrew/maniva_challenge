from django.forms import ModelForm
from django_countries.fields import CountryField
from djongo import models

class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    email = models.EmailField(verbose_name="Email", null=True, default=None, blank=True)
    subject = models.CharField(max_length=50, verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    country = CountryField(blank=True)
    objects = models.DjongoManager()

    def __str__(self):
        return self.name, self.email, self.subject, self.message

class Consultation(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.TextField()
    client_name = models.CharField(max_length=500, verbose_name="Client name")
    objects = models.DjongoManager()

    def __str__(self):
        return self.title, self.description, self.client_name

class LocationExpression(models.Model):
    pass



