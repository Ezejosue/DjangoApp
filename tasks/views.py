from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.utils import timezone

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
    tasks = Task.objects.filter(user=request.user, dateCompleted__isnull=True)
    return render(request, 'task.html', {'tasks': tasks})

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

# task Create view


def task_create(request):
    if request.method == 'GET':
        return render(request, 'create-task.html', {'form': TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            newTask = form.save(commit=False)
            newTask.user = request.user
            newTask.save()
            return redirect('task')
        except ValueError:
            return render(request, 'create-task.html', {'form': TaskForm, 'message': 'Bad data passed in. Try again.'})

# task detail view


def task_detail(request, id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task-detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('task')
        except ValueError:
            return render(request, 'task-detail.html', {'task': task, 'form': form, 'message': 'Bad info passed in. Try again.'})

# task complete view


def task_complete(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    if request.method == 'POST':
        task.dateCompleted = timezone.now()
        task.save()
        return redirect('task')

# task delete view


def task_delete(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task')
