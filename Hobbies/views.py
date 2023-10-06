from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby


# Create your views here.
def index(request):
    hobby_list = Hobby.objects.all()
    return HttpResponse(hobby_list)

