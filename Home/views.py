from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(
        'Hello! My name is Briella, welcome to my page! My pronouns are they/them and I like paleontology.')

