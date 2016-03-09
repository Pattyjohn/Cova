from django.conf.urls import url
from .views import LogInView, UserRegisterView
from . import views

urlpatterns = [
    url(r'^ingresar/$', LogInView.as_view(), name='login'),
    url(r'^salir/$', views.LogOut, name='logout'),
    url(r'^registrar/$', UserRegisterView.as_view(), name='register'),


]