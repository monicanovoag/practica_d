from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import *


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

@login_required
def perfil (request):
    return render (request,"perfil.html")

@login_required
def formulario (request):
    data = {
        "formFono": audio_fonoForm
    }

    if request.method == "POST":
        formu = audio_fonoForm(request.POST, request.FILES)
        if formu.is_valid():
            formu.save()
            messages.success(request,"Audio paciente registrado con éxito")
        else:
            messages.error(request,"Error, registro no realizado")

    return render (request,"formulario.html",data)