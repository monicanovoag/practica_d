from collections import Counter
from datetime import datetime
from collections import defaultdict
import os
import xlwt


from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
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

    return render (request,"formularios/formulario.html",data)

@login_required
def formulario_comunicativo(request):
    data = {
        "formComu": formulario_comunicacion(),
        "fecha_actual": datetime.now(),
    }

    if request.method == "POST":
        formu = formulario_comunicacion(request.POST)
        if formu.is_valid():
            formulario = formu.save(commit=False)  
            formulario.id_fono = request.user.id  
            formulario.save() 
            messages.success(request,"Información ingresada con éxito.")
        else:
            messages.error(request,"Error, registro no realizado. Por favor verifica la información ingresada")

    return render(request, "formularios/formulario_comunicativo.html", data)

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

    data = {}

    # Obtener la cuenta de usuarios por género
    genero_counts = audio_persona.objects.values('genero_usuario__nombre_genero').annotate(total=Count('id'))
    genero_data = {item['genero_usuario__nombre_genero']: item['total'] for item in genero_counts}
    data["genero_data"] = genero_data

    # Obtener los datos de los años de nacimiento
    anos_nacimiento = audio_persona.objects.values('ano_nac').annotate(total=Count('id')).order_by('ano_nac')
    labels = [str(item['ano_nac']) for item in anos_nacimiento]
    data_values = [item['total'] for item in anos_nacimiento]
    data["ano_nacimiento_data"] = {
        "labels": labels,
        "data": data_values
    }

    # Obtener la cuenta de usuarios por comuna
    comuna_counts = audio_persona.objects.values('comuna_usuario').annotate(total=Count('id'))
    comuna_data = {item['comuna_usuario']: item['total'] for item in comuna_counts}
    data["comuna_data"] = comuna_data

    # Preparar datos para el gráfico de barras
    labels = list(comuna_data.keys())
    data_values = list(comuna_data.values())

    # Renderizar el gráfico en formato JSON para pasarlo a la plantilla HTML
    data["bar_chart_data"] = {
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
    data["registros_diarios"] = {
        "fechas": fechas,
        "cantidades": cantidades
    }

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


def descargar_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="audio_fono.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('audio_fono')

    # Obtener todas las enfermedades únicas presentes en la tabla audio_fono
    enfermedades_unicas = OtrasEnf.objects.values_list('nombre_otras_enf', flat=True).distinct()

    # Escribir encabezados de columnas
    row_num = 0
    columns = ['ID', 'ID Usuario', 'Nombre Paciente', 'Género', 'Año de Nacimiento', 'Diagnóstico Fono'] + list(enfermedades_unicas) + ['Audio FO1', 'Audio FO2', 'Audio FO3', 'Audio FO4', 'Audio FO5', 'Fecha de Registro']
    for col_num, column_title in enumerate(columns):
        ws.write(row_num, col_num, column_title)

    # Escribir datos de la tabla audio_fono
    audio_fonos = audio_fono.objects.all()
    for audio in audio_fonos:
        row_num += 1
        ws.write(row_num, 0, audio.id)
        ws.write(row_num, 1, audio.id_usuario)
        ws.write(row_num, 2, audio.nombre_paciente)
        ws.write(row_num, 3, audio.genero_usuario.nombre_genero if audio.genero_usuario else '')  # Acceder al campo de género si existe
        ws.write(row_num, 4, audio.ano_nac)
        ws.write(row_num, 5, audio.tipo_diagnostico_flgo.nombre_diagnostico if audio.tipo_diagnostico_flgo else '')  # Acceder al campo de diagnóstico si existe

        # Marcar "Sí" o "No" para cada enfermedad única presente en esta fila
        for col_num, enfermedad in enumerate(enfermedades_unicas, start=6):
            if enfermedad in [enf.nombre_otras_enf for enf in audio.otras_enf.all()]:
                ws.write(row_num, col_num, "Sí")
            else:
                ws.write(row_num, col_num, "No")

        ws.write(row_num, 6 + len(enfermedades_unicas), audio.audio_fo1.name if audio.audio_fo1 else '')  # Acceder al campo de audio FO1 si existe
        ws.write(row_num, 7 + len(enfermedades_unicas), audio.audio_fo2.name if audio.audio_fo2 else '')  # Acceder al campo de audio FO2 si existe
        ws.write(row_num, 8 + len(enfermedades_unicas), audio.audio_fo3.name if audio.audio_fo3 else '')  # Acceder al campo de audio FO3 si existe
        ws.write(row_num, 9 + len(enfermedades_unicas), audio.audio_fo4.name if audio.audio_fo4 else '')  # Acceder al campo de audio FO4 si existe
        ws.write(row_num, 10 + len(enfermedades_unicas), audio.audio_fo5.name if audio.audio_fo5 else '')  # Acceder al campo de audio FO5 si existe
        ws.write(row_num, 11 + len(enfermedades_unicas), audio.fecha_registro.strftime('%Y-%m-%d %H:%M:%S'))  # Formatear la fecha como string

    wb.save(response)
    return response





def descargar_xls_persona(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="audio_persona.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('audio_persona')

    # Escribir encabezados de columnas
    row_num = 0
    columns = ['ID', 'WSP Usuario', 'Año de Nacimiento', 'Comuna de Residencia','Genero','Sistema de Salud','Audio Manychat','Audio Físico','Fecha Registro']
    for col_num, column_title in enumerate(columns):
        ws.write(row_num, col_num, column_title)

    # Escribir datos de la tabla audio_persona
    audio_personas = audio_persona.objects.all()
    for audio in audio_personas:
        row_num += 1
        ws.write(row_num, 0, audio.id)
        ws.write(row_num, 1, audio.wsp_usuario)
        ws.write(row_num, 2, audio.ano_nac)
        ws.write(row_num, 3, audio.comuna_usuario)
        ws.write(row_num, 4, audio.genero_usuario.nombre_genero if audio.genero_usuario else '')  
        ws.write(row_num, 5, audio.sistema_salud.nombre_sistema if audio.sistema_salud else '')  
        ws.write(row_num, 6, audio.audio_manychat)
        ws.write(row_num, 7, audio.audio_fisico if audio.audio_fisico else '')
        ws.write(row_num, 8, audio.fecha_registro_paciente.strftime('%Y-%m-%d %H:%M:%S'))  
    wb.save(response)
    return response


def descargar_audio_fisico(request, id_audio_persona):
    # Obtener la instancia de audio_persona
    audio = get_object_or_404(audio_persona, pk=id_audio_persona)

    # Verificar si hay un enlace de audio físico disponible
    if audio.audio_fisico:
        # Redirigir al usuario al enlace de audio físico para descargar
        return redirect(audio.audio_fisico)
    else:
        return HttpResponse("El enlace de audio físico no está disponible para descargar.")
    
@login_required
def resumen_paciente (request):

    formularios_usuario = formulario_com.objects.filter(id_fono=request.user.id).order_by('-id')

    data = {
        "fecha_actual" : datetime.now(),      
        "datos": formularios_usuario
    }
    return render (request,"resumen.html",data)


       