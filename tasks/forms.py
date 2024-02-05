from django.forms import ModelForm

from .models import Task

# Task Create Form


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
