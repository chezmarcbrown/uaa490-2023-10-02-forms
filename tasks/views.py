from django.shortcuts import render, redirect
from .forms import NewTaskForm, TaskNameForm, TaskForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Task

tasks = ['eat', 'sleep', 'pray'
]

def index(request):
    return render(request, 'tasks/index.html', {
        'tasks': tasks
    })

def add(request):
    return render(request, "tasks/add.html")

def add(request):
    return render(request, "tasks/add.html", {"form": NewTaskForm()})

def add(request):
    if request.method == "POST":
        task = request.POST["task"]
        priority = request.POST["priority"]
        tasks.append(task)
        #return HttpResponseRedirect(reverse('tasks:index'))

        return redirect('tasks:index')
    else:
        return render(request, "tasks/add.html", {"form": NewTaskForm()})

def add(request):
    if request.method == "POST":
        f = NewTaskForm(request.POST)
        if f.is_valid():
            task = request.POST["task"]
            priority = request.POST["priority"]
            tasks.append(task)
            return redirect('tasks:index')
        else:
            return render(request, 'tasks/add.html', {"form": f})
    else:
        return render(request, "tasks/add.html", {"form": NewTaskForm()})


def add(request):
    if request.method == "POST":
        f = NewTaskForm(request.POST)
        if f.is_valid():
            task = f.cleaned_data["task"]
            priority = f.cleaned_data["priority"]
            tasks.append(task)
            return redirect('tasks:index')
        else:
            return render(request, 'tasks/add.html', {"form": f})
    else:
        return render(request, "tasks/add.html", {"form": NewTaskForm()})

def add(request):
    if request.method == "POST":
        f = NewTaskForm(request.POST)
        if f.is_valid():
            task = f.cleaned_data["task"]
            priority = f.cleaned_data["priority"]
            if task not in tasks:
                tasks.append(task)
                messages.success(request, "Task added sent." )
                return redirect('tasks:index')
            else:
                return render(request, 'tasks/add.html', {
                    "form": f,
                    "errormessage": "Duplicate task not allowed"
                })
        else:
            return render(request, 'tasks/add.html', {"form": f})
    else:
        return render(request, "tasks/add.html", {"form": NewTaskForm()})

def delete(request, task):
    if task in tasks:
        tasks.remove(task)
    return redirect('tasks:index')

def delete(request):
    if request.method == "POST":
        f = TaskNameForm(request.POST)
        if f.is_valid():
            task = f.cleaned_data["task"]
            if task in tasks:
                tasks.remove(task)
                return redirect('tasks:index')
            else:
                return render(request, 'tasks/delete.html', {
                    "form": f,
                    "errormessage": "Cannot find task to delete"
                })
        else:
            return render(request, 'tasks/delete.html', {"form": f})
    else:
        return render(request, "tasks/delete.html", {"form": TaskNameForm()})

def index(request):
    return render(request, 'tasks/index.html', {
        'tasks': Task.objects.all()
    })

def add(request):
    if request.method == "POST":
        f = NewTaskForm(request.POST)
        if f.is_valid():
            task = f.cleaned_data["task"]
            priority = f.cleaned_data["priority"]
            if task not in tasks:
                t = Task(title=task, priority=priority)
                t.save()
#                tasks.append(task)
                messages.success(request, "Task added sent." )
                return redirect('tasks:index')
            else:
                return render(request, 'tasks/add.html', {
                    "form": f,
                    "errormessage": "Duplicate task not allowed"
                })
        else:
            return render(request, 'tasks/add.html', {"form": f})
    else:
        return render(request, "tasks/add.html", {"form": NewTaskForm()})


def add(request):
    if request.method == "POST":
        f = TaskForm(request.POST)
        if f.is_valid():
            task = f.cleaned_data["title"]
            priority = f.cleaned_data["priority"]
            if task not in tasks:
#                t = Task(title=task, priority=priority)
                f.save()
#                tasks.append(task)
                messages.success(request, "Task added sent." )
                return redirect('tasks:index')
            else:
                return render(request, 'tasks/add.html', {
                    "form": f,
                    "errormessage": "Duplicate task not allowed"
                })
        else:
            return render(request, 'tasks/add.html', {"form": f})
    else:
        return render(request, "tasks/add.html", {"form": TaskForm()})

