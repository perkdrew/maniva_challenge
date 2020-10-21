from django.urls import path
from maniva_webapp import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="webapp_index"),
    path("contact/", views.manage_contacts),
]