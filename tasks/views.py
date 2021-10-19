from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import taskForm

from .models import Task
from tasks import models

from tasks import forms

# Create your views here.
def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk = id)
    return render(request, 'tasks/task.html', {'task': task})

def newTask(request):
    if request.method == 'POST':
        form = taskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = taskForm()
        return render(request, 'tasks/addtask.html', {'form': form})