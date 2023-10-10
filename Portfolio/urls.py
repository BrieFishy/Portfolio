from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.portfolio, name="portfolio"),
    path('<int:item_id>', views.project_detail, name="project_detail"),
    path('hobbies/<int:item_id>', views.hobby_detail, name="hobby_detail"),
    path('home/', views.home, name="home"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('contact/', views.contact, name="contact"),
]

