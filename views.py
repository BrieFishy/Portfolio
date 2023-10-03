from django.shortcuts import redirect


def index(request):
    response = redirect('/home')
    return response

