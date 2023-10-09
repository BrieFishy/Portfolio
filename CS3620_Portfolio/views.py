from django.shortcuts import redirect


def index(request):
    response = redirect('portfolio/home')
    return response

