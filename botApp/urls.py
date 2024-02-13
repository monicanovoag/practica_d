from django.urls import path, include
from .views import *
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register(r'audiofono',views.audiofonoViewSet)

urlpatterns = [
 path('', home, name='home'),
 path('login/', login, name='login'),
 path('perfil/', perfil, name='perfil'),
 path('formulario/', formulario, name='formulario'),
 path('archivos/audios/<str:nombre_archivo>/', archivo, name='archivo_audio'),
 
 #API

 path('api/v1/', include(router.urls))


]

