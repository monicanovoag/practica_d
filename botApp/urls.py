from django.urls import path, include
from .views import *
from rest_framework import routers
from .import views

handler_404 = views.handler404

urlpatterns = [
 path('', home, name='home'),
 path('login/', login, name='login'),
 path('perfil/', perfil, name='perfil'),
 path('formulario/', formulario, name='formulario'),
 path('archivos/audios/<str:nombre_archivo>/', archivo, name='archivo_audio'),
 

 #ACCESO A ADMIN DJANGO
 path('admin/', admin, name="admin_django"),
 
 #ACCESO AUDIOS 
 path('admin/botApp/audio_persona/', admin_audios_persona, name="admin_audios_persona"),

 #API

 path('api_home/',api, name='api'),
 path('view_audio_fonos/', AudioFonoAPIView.as_view(), name="api_audio_fonos"),



]

