from collections import Counter
from datetime import datetime
from collections import defaultdict
import os

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Count
from django.db.models.functions import TruncDate

import matplotlib.pyplot as plt

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .forms import *
from .models import *
from .serializer import *




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
            response = HttpResponse(archivo.read(), content_type='audio/ogg')
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


class audio_personaViewSet(viewsets.ModelViewSet):
    queryset = audio_persona.objects.all()
    serializer_class = audio_personaSerializer


@login_required
def reporte_persona(request):

    # Inicializar data como un diccionario vacío
    data = {}

    # Obtener la cuenta de usuarios por género
    genero_counts = audio_persona.objects.values('genero_usuario__nombre_genero').annotate(total=Count('id'))
    genero_data = {item['genero_usuario__nombre_genero']: item['total'] for item in genero_counts}

    # Agregar los datos del género al diccionario data
    data["genero_data"] = genero_data

    # Obtener los datos de los años de nacimiento
    datos_audio_fono = audio_persona.objects.all()
    anos_nacimiento = {}
    for dato in datos_audio_fono:
        ano = dato.ano_nac
        if ano in anos_nacimiento:
            anos_nacimiento[ano] += 1
        else:
            anos_nacimiento[ano] = 1
    labels = list(anos_nacimiento.keys())
    data_values = list(anos_nacimiento.values())
    data["ano_nacimiento_data"] = {
        "labels": labels,
        "data": data_values
    }

    # Obtener la cuenta de usuarios por sistema de salud
    sistema_salud_counts = audio_persona.objects.values('sistema_salud__nombre_sistema').annotate(total=Count('id'))
    sistema_salud_data = {item['sistema_salud__nombre_sistema']: item['total'] for item in sistema_salud_counts}

    data["sistema_salud_data"] = sistema_salud_data

    # Consulta para agrupar por día y contar registros
    registros_diarios = audio_persona.objects.annotate(
        dia_registro=TruncDate('fecha_registro_paciente')
    ).values('dia_registro').annotate(
        total=Count('id')
    ).order_by('dia_registro')

    # Convertir datos a formato adecuado para el gráfico
    fechas = [registro['dia_registro'].strftime('%Y-%m-%d') for registro in registros_diarios]
    cantidades = [registro['total'] for registro in registros_diarios]

    # Pasar los datos al template
    data["registros_diarios"] = {
        "fechas": fechas,
        "cantidades": cantidades
    }

    # Agregar la fecha actual al diccionario data
    data["fecha_actual"] = datetime.now()


    return render(request, "reportes/reporte_persona.html", data)

@login_required

def reporte_fono(request):
    # Inicializar data como un diccionario vacío
    data = {}

    # Obtener la cuenta de usuarios por género
    genero_counts = audio_fono.objects.values('genero_usuario__nombre_genero').annotate(total=Count('id'))
    genero_data = {item['genero_usuario__nombre_genero']: item['total'] for item in genero_counts}
    data["genero_data"] = genero_data

    # Obtener los datos de los años de nacimiento
    datos_audio_fono = audio_fono.objects.all()
    anos_nacimiento = {}
    for dato in datos_audio_fono:
        ano = dato.ano_nac
        if ano in anos_nacimiento:
            anos_nacimiento[ano] += 1
        else:
            anos_nacimiento[ano] = 1
    labels = list(anos_nacimiento.keys())
    data_values = list(anos_nacimiento.values())
    data["ano_nacimiento_data"] = {
        "labels": labels,
        "data": data_values
    }

    # Obtener la cuenta de tipos de diagnóstico
    tipo_diagnostico_counts = audio_fono.objects.values('tipo_diagnostico_flgo__nombre_diagnostico').annotate(total=Count('id'))
    tipo_diagnostico_data = {item['tipo_diagnostico_flgo__nombre_diagnostico']: item['total'] for item in tipo_diagnostico_counts}
    data["tipo_diagnostico_data"] = tipo_diagnostico_data

    # Obtener los datos de cada otra_enf
    otras_enf_data = {}
    for otra_enf in OtrasEnf.objects.all():
        count = otra_enf.audio_fono_set.count()
        otras_enf_data[otra_enf.nombre_otras_enf] = {
            "labels": [otra_enf.nombre_otras_enf],
            "data": [count]
        }
    data["otras_enf_data"] = otras_enf_data

    # Consulta para agrupar por día y contar registros
    registros_diarios = audio_fono.objects.annotate(
        dia_registro=TruncDate('fecha_registro')
    ).values('dia_registro').annotate(
        total=Count('id')
    ).order_by('dia_registro')

    # Convertir datos a formato adecuado para el gráfico
    fechas = [registro['dia_registro'].strftime('%Y-%m-%d') for registro in registros_diarios]
    cantidades = [registro['total'] for registro in registros_diarios]

    # Pasar los datos al template
    data["registros_diarios"] = {
        "fechas": fechas,
        "cantidades": cantidades
    }

    # Agregar la fecha actual al diccionario data
    data["fecha_actual"] = datetime.now()

    return render(request, "reportes/reporte_fono.html", data)
