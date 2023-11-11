from django.urls import path
from . import views
from django import forms


urlpatterns = [
    path('' ,views.index),
    path('schoolapp/about/' ,views.about, name='about'),
    path('schoolapp/login/' ,views.login, name='login'),
    path('schoolapp/register/' ,views.register,name='register'),
    path('register/', views.register, name='register'),
    path('login/' ,views.login, name='login'),
    path('newpage/' ,views.newpage, name='newpage'),
    path('forms/' ,views.forms, name='forms'),
]



