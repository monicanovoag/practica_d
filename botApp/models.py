from django.db import models
from django.utils import timezone

# Create your models here.


class tipo_diagnostico_flgo(models.Model):


    id = models.AutoField(primary_key=True, verbose_name="id_etiqueta") 
    nombre_diagnostico = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_diagnostico
    

class genero_usuario(models.Model):

    FEMENINO = "Femenino"
    MASCULINO = "Masculino"
    OTRO = "Otro"

    GENERO_CHOICES = [
        (FEMENINO, "Femenino"),
        (MASCULINO, "Masculino"),
        (OTRO, "Otro"),]
    
    id = models.AutoField(primary_key=True, verbose_name="id_genero") 
    nombre_genero = models.CharField(max_length=20, choices=GENERO_CHOICES)


    def __str__(self):
        return self.nombre_genero
    
class tipo_usuario(models.Model):

    USUARIO = "Usuario"
    PACIENTE = "Paciente"
    ADMIN = "admin"

    USUARIOS_CHOICES = [
        (USUARIO, "Usuario"),
        (PACIENTE, "Paciente"),
        (ADMIN, "Admin"),]

    id = models.AutoField(primary_key=True, verbose_name="id_tipo_usuario")
    nombre_tipo_usuario = models.CharField(max_length=20, choices=USUARIOS_CHOICES)

    def __str__(self):
        return self.nombre_tipo_usuario
    
class audio_persona(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_audio")
    wsp_usuario = models.CharField(max_length = 30) 
    ano_nac = models.CharField(max_length=10, verbose_name="año_nacimiento")
    comuna_residencia = models.CharField(max_length=30, verbose_name="comuna_residencia")
    genero_usuario = models.ForeignKey(genero_usuario, on_delete=models.CASCADE)    
    sistema_salud = models.CharField(max_length=10)
    audio_manychat = models.CharField(max_length=255)    
    fecha_registro_paciente = models.DateTimeField(default=timezone.now)
       
class audio_fono(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_audio") 
    id_usuario = models.IntegerField()
    nombre_paciente = models.CharField(max_length=20)
    audio_fo1 = models.FileField(upload_to='audios/fono/')
    audio_fo2 = models.FileField(upload_to='audios/fono/', blank=True, null=True)
    audio_fo3 = models.FileField(upload_to='audios/fono/', blank=True, null=True)
    audio_fo4 = models.FileField(upload_to='audios/fono/', blank=True, null=True)
    audio_fo5 = models.FileField(upload_to='audios/fono/', blank=True, null=True)
    ano_nac = models.CharField(max_length=10, verbose_name="Año Nacimiento")
    fecha_registro = models.DateTimeField(default=timezone.now)
    otras_enfermedades = models.CharField(max_length=50)

    genero_usuario = models.ForeignKey(genero_usuario, on_delete=models.CASCADE)
    tipo_diagnostico_flgo = models.ForeignKey(tipo_diagnostico_flgo, on_delete=models.CASCADE)

