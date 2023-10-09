from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.portfolio, name="portfolio"),
    path('home/', views.home, name="home"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('contact/', views.contact, name="contact"),
]

