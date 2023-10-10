from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Hobby
from django.template import loader


# Create your views here.
def portfolio(request):
    project_list = Project.objects.all()
    context = {
        'project_list': project_list,
    }
    return render(request, 'portfolio/index.html', context)


def project_detail(request, item_id):
    item = Project.objects.get(pk=item_id)
    context = {
        'name': item.project_name,
        'description': item.project_description,
        'image': item.project_image,
    }
    return render(request, 'portfolio/detail.html', context)


def contact(request):
    return render(request, 'portfolio/contact.html', {})


def hobbies(request):
    hobby_list = Hobby.objects.all()
    context = {
        'hobby_list': hobby_list,
    }
    return render(request, 'portfolio/hobbies.html', context)


def hobby_detail(request, item_id):
    item = Hobby.objects.get(pk=item_id)
    context = {
        'name': item.hobby_name,
        'description': item.hobby_description,
        'image': item.hobby_image,
    }
    return render(request, 'portfolio/detail.html', context)


def home(request):
    return render(request, 'portfolio/home.html', {})
