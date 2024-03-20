from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser, PermissionsMixin, Group, Permission
from django.utils import timezone
# Create your models here.

class tipo_usuario(models.Model):

    id = models.AutoField(primary_key=True, verbose_name="id_tipo_usuario")
    nombre_tipo_usuario = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_tipo_usuario

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('El email debe ser obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe ser staff')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe ser superusuario')
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    username = None

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def get_full_name(self):
        return f'{self.nombre} {self.apellido}'
    
    def get_short_name(self):
        return self.nombre or self.email.split('@')[0]