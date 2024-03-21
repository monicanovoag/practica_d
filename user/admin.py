from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, tipo_usuario, Log

      


class tipo_usuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_tipo_usuario']
    search_fields = ['nombre_tipo_usuario']

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username','email', 'nombre', 'apellido','tipo_usuario','is_staff', 'is_superuser']
    search_fields = ['email', 'nombre', 'apellido']
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Información personal', {'fields': ('nombre', 'apellido','tipo_usuario')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'nombre', 'apellido','tipo_usuario', 'password1', 'password2', 'is_staff', 'is_superuser')
        }),
    )
    ordering = ['email']

class LogInicioSesionAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'fecha_inicio', 'texto']

admin.site.register(Log, LogInicioSesionAdmin)        
admin.site.register(tipo_usuario)
admin.site.register(User, CustomUserAdmin)
