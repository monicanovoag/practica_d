from django.urls import path, include
from .views import *



urlpatterns = [
 path('', home, name='home'),
 path('login/', login, name='login'),
 path('perfil/', perfil, name='perfil'),
 path('formulario/', formulario, name='formulario'),
 path('archivos/audios/<str:nombre_archivo>/', archivo, name='archivo_audio'),
]

