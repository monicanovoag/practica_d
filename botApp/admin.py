from django.contrib import admin
from .models import *
from django.http import HttpResponse
from django.urls import reverse
import requests
from django.utils.html import format_html

def download_audios(modeladmin, request, queryset):
    import zipfile
    import io

    # Crear un archivo ZIP en memoria
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for audio in queryset:
            # Iterar sobre los campos de audio y agregar al archivo ZIP si contienen archivos
            for i in range(1, 6):  # Iterar sobre los campos audio_fo1 a audio_fo5
                audio_field_name = f'audio_fo{i}'
                audio_file = getattr(audio, audio_field_name)
                if audio_file:
                    # Descargar el archivo de la URL y agregarlo al archivo ZIP
                    response = requests.get(request.build_absolute_uri(audio_file.url))
                    if response.status_code == 200:
                        zip_file.writestr(audio_file.name.split('/')[-1], response.content)

    # Configurar la respuesta HTTP para descargar el archivo ZIP
    response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="audios.zip"'
    return response

download_audios.short_description = "Descargar audios seleccionado/s"

class generoAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_genero")

class diagnosticoAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_diagnostico")

class otras_enfAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_otras_enf")

class sistema_saludAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_sistema")


class audiofonoAdmin(admin.ModelAdmin):
    actions = [download_audios]
    list_display = ("id","id_usuario","nombre_paciente","genero_usuario","ano_nac","tipo_diagnostico_flgo","otras_enfermedades","audio_fo1","audio_fo2","audio_fo3","audio_fo4","audio_fo5","fecha_registro")

    def otras_enfermedades(self, obj):
        return ', '.join([otras.nombre_otras_enf for otras in obj.otras_enf.all()])
    otras_enfermedades.short_description = 'Otras Enfermedades'


class audioPersonaAdmin(admin.ModelAdmin):
    list_display = ("id","wsp_usuario","ano_nac","genero_usuario","sistema_salud","comuna_usuario","audio_manychat","audio_fisico","fecha_registro_paciente")
    
    def descargar_audio_fisico(self, obj):
        if obj.audio_fisico:
            return format_html('<a href="{}" download>Descargar audio físico</a>', obj.audio_fisico)
        else:
            return "No disponible"

    descargar_audio_fisico.short_description = "Audio Físico"


#FORMULARIO SOCIOCOMUNICATIVO 

class relacionAdmin(admin.ModelAdmin):
    list_display = ('id','tipo_relacion')

class frecuenciaAdmin(admin.ModelAdmin):
    list_display = ('id','tipo_frecuencia')

class duracionAdmin(admin.ModelAdmin):
    list_display = ('id','tipo_duracion')

class funcionAdmin(admin.ModelAdmin):
    list_display = ('id','tipo_funcion')
    
class satisfaccionAdmin(admin.ModelAdmin):
    list_display = ('id','tipo_satisfaccion')

class formConvAdmin(admin.ModelAdmin):
    list_display = ('id','id_fono', 'nombre', 'ano_nac', 'genero_usuario',
                    'tipo_relacion_1', 'frecuencia_1', 'duracion_1', 'funcion_1', 'satisfaccion_1','complemento_1',
                    'tipo_relacion_2', 'frecuencia_2', 'duracion_2', 'funcion_2', 'satisfaccion_2','complemento_2',
                    'tipo_relacion_3', 'frecuencia_3', 'duracion_3', 'funcion_3', 'satisfaccion_3','complemento_3',
                    'tipo_relacion_4', 'frecuencia_4', 'duracion_4', 'funcion_4', 'satisfaccion_4','complemento_4')

               
admin.site.register(genero_usuario,generoAdmin)
admin.site.register(tipo_diagnostico_flgo,diagnosticoAdmin)
admin.site.register(audio_fono,audiofonoAdmin)
admin.site.register(audio_persona,audioPersonaAdmin)
admin.site.register(OtrasEnf, otras_enfAdmin)
admin.site.register(sistema_salud, sistema_saludAdmin)

admin.site.register(tipo_relacion,relacionAdmin)
admin.site.register(frecuencia_conv,frecuenciaAdmin)
admin.site.register(duracion_conv,duracionAdmin)
admin.site.register(funcion_conv,funcionAdmin)
admin.site.register(satisfaccion_conv,satisfaccionAdmin)
admin.site.register(formulario_com,formConvAdmin)





