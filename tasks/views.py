from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
                return render(request, 'signup.html', {'form': UserCreationForm, 'message': 'User created successfully'})
            except:
                return render(request, 'signup.html', {'form': UserCreationForm, 'message': 'User already exists'})
        return render(request, 'signup.html', {'form': UserCreationForm, 'message': 'Passwords did not match'})