#Django
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import BaseBackend


def log_in(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not none:
        login(request, user)
        return f'Succesful login'
    else: 
        return f'Unsuccesfrul login, please try again'


