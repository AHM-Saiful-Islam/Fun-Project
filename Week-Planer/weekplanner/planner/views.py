from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.
def week_planner(request):
    tasks = Task.objects.all().order_by('day', 'time')
    return render(request, 'planner/week_planner.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('week_planner')
    else:
        form = TaskForm()
    return render(request, 'planner/add_task.html', {'form': form})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # Toggle completion status
    task.save()
    return redirect('week_planner')