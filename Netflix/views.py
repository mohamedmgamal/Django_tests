from django.shortcuts import render,redirect
from django.http import HttpResponse
from Netflix.models import Movies,Categories
from Netflix.forms import MovieForm,Categories
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.
@login_required(login_url='/auth/login/')
def viewAll(request):
    movies=Movies.objects.all()
    return render(request,"showAll.html",{"movies":movies})
@login_required(login_url='/auth/login/')
@permission_required('Netflix.Can_add_movies')
def addMovie(request):
    form=MovieForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("viewAll")
    return render(request,"addMovie.html",{
        'form':form
    })
@login_required(login_url='/auth/login/')
@permission_required('Netflix.Can_add_movies')
def edit(request,id):
        form = MovieForm(request.POST or None, request.FILES or None,instance=Movies.objects.get(pk=id))
        if form.is_valid():
            form.save()
            return redirect("viewAll")
        return render(request, "editMovie.html", {
            'form': form
            ,'id':id
        })
@login_required(login_url='/auth/login/')
def delete(request,id):
    Movies.objects.get(pk=id).delete()
    return redirect("viewAll")