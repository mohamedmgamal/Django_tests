from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movies
# Create your views here.
def empty(request):
    return HttpResponse("empty moview url")

def createCategory(request):
    return HttpResponse("empty moview url")

def createMovie(request):
    return HttpResponse("empty moview url")


def viewAll(request):
    tasks=Movies.objects.all()
    return render(request,"index.html",{
        'movies':tasks
    })