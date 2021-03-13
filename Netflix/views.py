from django.shortcuts import render,redirect
from django.http import HttpResponse
from Netflix.models import Movies,Categories
from Netflix.forms import MovieForm,Categories
# Create your views here.
def viewAll(request):
    movies=Movies.objects.all()
    return render(request,"showAll.html",{"movies":movies})

def addMovie(request):
    form=MovieForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("viewAll")
    return render(request,"addMovie.html",{
        'form':form
    })