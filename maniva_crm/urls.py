from django.urls import path
from maniva_crm import views


urlpatterns = [
    path("crm/register/", views.registerPage, name="register"),
    path("crm/login/", views.loginPage, name="login"),
    path("crm/logout/", views.logoutUser, name="logout"),
    path("crm/", views.home, name="home"),
    path("crm/user/", views.userPage, name="user-page"),
    path("crm/services/", views.services, name="services"),
    path("crm/customer/<str:pk_test>/", views.customer, name="customer"),
    path("crm/create_order/<str:pk>/", views.createOrder, name="create_order"),
    path("crm/update_order/<str:pk>/", views.updateOrder, name="update_order"),
    path("crm/delete_order/<str:pk>/", views.deleteOrder, name="delete_order"),
]