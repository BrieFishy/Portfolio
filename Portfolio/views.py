from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .models import Hobby


# Create your views here.
def portfolio(request):
    project_list = Project.objects.all()
    return HttpResponse(project_list)


def contact(request):
    return HttpResponse(
        'jrutherford@mail.weber.edu')


def hobbies(request):
    hobby_list = Hobby.objects.all()
    return HttpResponse(hobby_list)


def home(request):
    return HttpResponse(
        'Hello! My name is Briella, welcome to my page! My pronouns are they/them and I like paleontology.')
