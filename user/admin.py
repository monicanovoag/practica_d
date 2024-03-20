from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, tipo_usuario


class tipo_usuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_tipo_usuario']
    search_fields = ['nombre_tipo_usuario']

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'nombre', 'apellido','is_staff', 'is_superuser']
    search_fields = ['email', 'nombre', 'apellido']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información personal', {'fields': ('nombre', 'apellido')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre', 'apellido', 'password1', 'password2', 'is_staff', 'is_superuser')
        }),
    )
    ordering = ['email']


admin.site.register(tipo_usuario)
admin.site.register(User, CustomUserAdmin)

