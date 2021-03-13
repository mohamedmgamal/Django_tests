from django.http import HttpResponse
from django.shortcuts import render,redirect
gName=""
tasks=[]
def index(request):
    if request.method=="POST" and not request.POST['task']=="":
        tasks.append(request.POST['task'])
    print(tasks)
    return render(request , "index.html",{
        "name":"Mohamed Gamal",
        "tasks":tasks
    })
def delete(request):
    if request.method=="POST":
        tasks.remove(request.POST['task'])
    return redirect("index")

def welcome(request,name):
    return render(request,"hello.html",{
        "name":name
    })