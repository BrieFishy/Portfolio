from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


# Create your views here.
def index(request):
    project_list = Project.objects.all()
    return HttpResponse(project_list)

