from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
# Create your views here.
def signUp(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        user=authenticate(username=form.cleaned_data.get("username"),password=form.cleaned_data.get("password1"))
        if user:
            login(request,user)
            return redirect("viewAll")

    return render(request,"registration/signUp.html",{"form":form})