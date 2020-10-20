from django.urls import path
from maniva_crm import views


urlpatterns = [
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("", views.home, name="home"),
    path("user/", views.userPage, name="user-page"),
    path("products/", views.products, name="products"),
    path("customer/<str:pk_test>/", views.customer, name="customer"),
    path("create_order/<str:pk>/", views.createServiceOrder, name="create_order"),
    path("update_order/<str:pk>/", views.updateServiceOrder, name="update_order"),
    path("delete_order/<str:pk>/", views.deleteServiceOrder, name="delete_order"),
]