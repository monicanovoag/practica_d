from django.contrib import admin
from .models import *

class generoAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_genero")

class etiquetaAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_etiqueta")

class tipousuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_tipo_usuario")

class audiofonoAdmin(admin.ModelAdmin):
    list_display = ("id","id_fono","audio_fo","genero_usuario","ano_nac","fecha_registro")

class audioPersonaAdmin(admin.ModelAdmin):
    list_display = ("id","audio_us","wsp_usuario","ano_nac","fecha_registro_paciente")


admin.site.register(genero_usuario,generoAdmin)
admin.site.register(audio_etiqueta,etiquetaAdmin)
admin.site.register(audio_fono,audiofonoAdmin)
admin.site.register(audio_persona,audioPersonaAdmin)
admin.site.register(tipo_usuario, tipousuarioAdmin)





