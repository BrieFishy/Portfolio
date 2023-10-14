from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Portfolio urls
    path('', views.portfolio, name="portfolio"),
    path('<int:project_id>', views.project_detail, name="project_detail"),
    path('add', views.add_project, name="add_project"),
    path('update/<int:project_id>', views.update_project, name="update_project"),
    path('delete/<int:project_id>', views.delete_project, name="delete_project"),

    # Hobby urls
    path('hobbies/', views.hobbies, name="hobbies"),
    path('hobbies/<int:hobby_id>', views.hobby_detail, name="hobby_detail"),
    path('home/', views.home, name="home"),

    # Contact urls
    path('contact/', views.contact, name="contact"),
    path('contact/add', views.add_contact, name="add_contact"),
]

