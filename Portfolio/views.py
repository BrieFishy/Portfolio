from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Hobby, Contact
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def portfolio(request):
    project_list = Project.objects.all()
    context = {
        'project_list': project_list,
    }
    return render(request, 'portfolio/index.html', context)


def project_detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    context = {
        'name': project.project_name,
        'description': project.project_description,
        'image': project.project_image,
        'proj_id': project_id,
    }
    return render(request, 'portfolio/detail.html', context)


@login_required
def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            # save to the database
            form.save()
        else:
            print(form.errors)
        # redirect to portfolio page
        return redirect('portfolio')
    else:
        return render(request, 'portfolio/editProject.html', {'form': ProjectForm()})


@login_required
def update_project(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            # save to the database
            form.save()
            # redirect to portfolio page
            return redirect('portfolio')
    else:
        return render(request, 'portfolio/editProject.html', {'form': ProjectForm(instance=project)})


@login_required
def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == "POST":
        project.delete()
        # redirect to portfolio page
        return redirect('portfolio')
    else:
        context = {
            'name': project.project_name,
            'description': project.project_description,
            'image': project.project_image,
            'proj_id': project_id,
            'delete_form': True,
        }
        return render(request, 'portfolio/detail.html', context)


def contact(request):
    contact_list = Contact.objects.all()
    context = {
        'contact_list': contact_list,
    }
    return render(request, 'portfolio/contact.html', context)


def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # save to the database
            form.save()
            # redirect to contact page
            return redirect('contact')
    else:
        return render(request, 'portfolio/addContact.html', {'form': ContactForm()})


def hobbies(request):
    hobby_list = Hobby.objects.all()
    context = {
        'hobby_list': hobby_list,
    }
    return render(request, 'portfolio/hobbies.html', context)


def hobby_detail(request, hobby_id):
    item = Hobby.objects.get(pk=hobby_id)
    context = {
        'name': item.hobby_name,
        'description': item.hobby_description,
        'image': item.hobby_image,
    }
    return render(request, 'portfolio/detail.html', context)


def home(request):
    return render(request, 'portfolio/home.html', {})
