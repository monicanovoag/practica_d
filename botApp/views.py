from django.shortcuts import render, redirect
from django.contrib import auth


# Create your views here.


def home (request):
    return render (request,"home.html")

def login (request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("perfil")
        else:
            return render(request, "registration/login.html")
        
    return render (request,"registration/login.html")

def perfil (request):
    return render (request,"perfil.html")