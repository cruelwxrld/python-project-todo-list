from django import forms
from .models import Task

class TaskForm(forms.Form):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {}
        labels = {
            'title': 'Task Title',
            'description': 'Task Description',
            'completed': 'Task Completed',
        }