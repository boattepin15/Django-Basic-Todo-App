from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task


def add_task(request):
    #ฟังก์ชัน เพิ่ม todo list
    task_req = request.POST['task']
    Task.objects.create(task=task_req)
    return redirect('home-page')

def mask_as_complate(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home-page')

def mask_as_doing(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home-page')

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home-page')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        new_task = request.POST['task']
        task.task = new_task
        task.save()
        return redirect('home-page')
    else:
        context = {
            'task':task
        }
        return render(request, 'edit_task.html', context)


