from django.urls import path, include
from .views import *
from rest_framework import routers
from .import views


handler_404 = views.handler404
router = routers.DefaultRouter()
router.register(r'audio_persona', views.audio_personaViewSet)

urlpatterns = [
 path('', home, name='home'),
 path('login/', login, name='login'),
 path('perfil/', perfil, name='perfil'),
 path('formulario/', formulario, name='formulario'),
 path('reporte_fono/', reporte_fono, name='reporte_fono'),
 path('reporte_persona/', reporte_persona, name='reporte_persona'),
 path('descargar-xls/', descargar_xls, name='descargar_xls'),
 path('descargar-xls-persona/', descargar_xls_persona, name='descargar_xls_persona'),

 path('archivos/audios/fono/<str:nombre_archivo>/', archivo_fono, name='archivo_audio'),
 path('archivos/audios/persona/<str:nombre_archivo>/', archivo_persona, name='archivo_audio'),

 
 
 #ACCESO AUDIOS 
 path('admin/botApp/audio_fono/', admin_audios_fono, name="admin_audios_fono"),
 path('admin/botApp/audio_persona/', admin_audios_persona, name="admin_audios_persona"),
 path('descargar_audio_fisico/<int:id_audio_persona>/', descargar_audio_fisico, name='descargar_audio_fisico'),


 #API
 path('api_home/',api, name='api'),
 path('view_audio_fonos/', AudioFonoAPIView.as_view(), name="api_audio_fonos"),
 path('view_audio_personas/', AudioPersonaAPIView.as_view(), name="api_audio_personas"),
 path('api/', include(router.urls)),

] 

