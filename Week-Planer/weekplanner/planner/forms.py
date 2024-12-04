from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'day', 'time', 'date']
        widgets = {
            'time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }