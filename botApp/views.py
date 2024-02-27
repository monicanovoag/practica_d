from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import os
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.urls import reverse
from django.http import HttpResponseRedirect




# Create your views here.


def home (request):

    data = {
        "fecha_actual" : datetime.now()       
    }
    return render (request,"home.html",data)

def login (request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            messages.success(request,"Inicio de sesión exitoso")
            return redirect("perfil")
        else:
            messages.error(request,"No fue posible iniciar sesión, inténtelo nuevamente")
            return render(request, "registration/login.html")
        
  
    return render (request,"registration/login.html")

@login_required
def perfil (request):

    data = {
        "fecha_actual" : datetime.now(), 
        "nombre_usuario" : request.user.first_name      
    }

    return render (request,"perfil.html", data)

@login_required
def formulario (request):
    data = {
        "formFono": audio_fonoForm,
        "fecha_actual" : datetime.now()
    }
    

    if request.method == "POST":
        formu = audio_fonoForm(request.POST, request.FILES)
        if formu.is_valid():
            formu.instance.id_usuario = request.user.id
            formu.save()
            messages.success(request,"Audio paciente registrado con éxito")
        else:
            messages.error(request,"Error, registro no realizado. Por favor verifica la información ingresada")

    return render (request,"formulario.html",data)

def archivo_fono(request, nombre_archivo):
    ruta_archivo = 'archivos/audios/fono/' + nombre_archivo 

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'rb') as archivo:
            response = HttpResponse(archivo.read(), content_type='audio/mpeg')
            return response
    else:

        return HttpResponse("El archivo solicitado no existe", status=404)
    
def archivo_persona(request, nombre_archivo):
    ruta_archivo = 'archivos/audios/persona/' + nombre_archivo 

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'rb') as archivo:
            response = HttpResponse(archivo.read(), content_type='audio/mpeg')
            return response
    else:

        return HttpResponse("El archivo solicitado no existe", status=404)
    
#API
@login_required
def api(request):
    data = {
        "fecha_actual" : datetime.now()       
    }
    return render (request,"api/api_home.html",data)



class AudioFonoAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        audio_fonos = audio_fono.objects.all()
        serializer = audio_fonoSerializer(audio_fonos, many=True)
        return Response(serializer.data)
    
class AudioPersonaAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        audio_personas = audio_persona.objects.all()
        serializer = audio_personaSerializer(audio_personas, many=True)
        return Response(serializer.data)


def admin_audios_fono (request):

    admin_url = reverse('admin:botApp_audio_fono_changelist')

    return HttpResponseRedirect(admin_url)

def admin_audios_persona (request):

    admin_url = reverse('admin:botApp_audio_persona_changelist')

    return HttpResponseRedirect(admin_url)


def admin (request):

    data = {
        "fecha_actual" : datetime.now()       
    }
    return render (request,"admin.html",data)

def handler404(request, exception):
    return render (request, "404.html", status=404)
