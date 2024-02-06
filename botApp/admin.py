from django.contrib import admin
from .models import *

class generoAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_genero")

class etiquetaAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_etiqueta")

class audiofonoAdmin(admin.ModelAdmin):
    list_display = ("id","audio_fo","ano_nac","fecha_ingreso_fono")

class audioPersonaAdmin(admin.ModelAdmin):
    list_display = ("id","audio_us","wsp_usuario","ano_nac","fecha_ingreso_persona")

class usuarioAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_usuario","apellido_usuario","correo_usuario","tipo_usuario")

admin.site.register(genero_usuario,generoAdmin)
admin.site.register(audio_etiqueta,etiquetaAdmin)
admin.site.register(audio_fono,audiofonoAdmin)
admin.site.register(audio_persona,audioPersonaAdmin)
admin.site.register(usuario,usuarioAdmin)





