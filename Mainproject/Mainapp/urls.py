from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index, name='Index'),
    path('Register/', views.Register, name='Register'),
    path('Login/', views.Login, name='Login'),
    path('Reg_Done/', views.Reg_Done, name='Reg_Done'),
]