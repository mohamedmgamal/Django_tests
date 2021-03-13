from django.shortcuts import render,redirect
from django.http import HttpResponse
from tasks.models import Task
# Create your views here.
def empty(request):
    return HttpResponse("empty page")
def viewAll(request):
    tasks=Task.objects.all()
    print(tasks)
    return render(request,"showAllTasks.html",{
        'tasks':tasks
    })
def delete(request,id):
    Task.objects.get(pk=id).delete()
    return redirect('viewAllTasks')
def addTask(request):
    if request.method=="POST":
        task=Task(title=request.POST["title"],description=request.POST["description"])
        task.save()
        return redirect('viewAllTasks')
    return render(request,'addTask.html')
def update(request,id):
    task=Task.objects.get(pk=id)
    if request.method=="POST":
        task.title=request.POST["title"]
        task.description=request.POST["description"]
        task.save()
        return redirect('viewAllTasks')
    return render(request,'update.html',{
        "task":task
    })