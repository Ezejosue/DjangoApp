from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.

# Home View


def home(request):
    return render(request, 'home.html')

# Sign Up View


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('task')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm, 'message': 'User already exists'})
        return render(request, 'signup.html', {'form': UserCreationForm, 'message': 'Passwords did not match'})

# Tasks View


def tasks(request):
    return render(request, 'task.html')

# Logout View


def logoutUser(request):
    logout(request)
    return redirect('home')

# Login View


def loginView(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'form': AuthenticationForm, 'message': 'Username or password did not match'})
        else:
            login(request, user)
            return redirect('task')
