from django.db import models
from django.utils import timezone

# Create your models here.


class audio_etiqueta(models.Model):

    DISARTRIA = "Disartria"
    DISFAGIA = "Disfagia"
    VOZ_Y_HABLA = "Voz_Habla"
    OTRO = "Otro"

    ETIQUETA_CHOICES = [
        (DISARTRIA, "Disartria"),
        (DISFAGIA, "Disfagia"),
        (VOZ_Y_HABLA, "Voz_Habla"),
        (OTRO, "Otro"),]

    id = models.AutoField(primary_key=True, verbose_name="id_etiqueta") 
    nombre_etiqueta = models.CharField(max_length=20, choices=ETIQUETA_CHOICES)

    def __str__(self):
        return self.nombre_etiqueta
    

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
    audio_us = models.FileField(upload_to='audios/')
    wsp_usuario = models.IntegerField()
    ano_nac = models.CharField(max_length=10, verbose_name="año_nacimiento")
    fecha_registro_paciente = models.CharField(max_length=15)

    genero_usuario = models.ForeignKey(genero_usuario, on_delete=models.CASCADE)
    audio_etiqueta = models.ForeignKey(audio_etiqueta, on_delete=models.CASCADE)

class audio_fono(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_audio") 
    id_paciente_ingresado = models.CharField(max_length=10, verbose_name="Id Paciente")
    audio_fo = models.FileField(upload_to='audios/')
    ano_nac = models.CharField(max_length=10, verbose_name="Año Nacimiento")
    fecha_registro = models.CharField(max_length=15)

    genero_usuario = models.ForeignKey(genero_usuario, on_delete=models.CASCADE)
    audio_etiqueta = models.ForeignKey(audio_etiqueta, on_delete=models.CASCADE)

class usuarioBot (models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_usuario")
    nombre_usuario = models.CharField(max_length=20)
    apellido_usuario = models.CharField(max_length=20)
    correo_usuario = models.EmailField(max_length=40)
    contrasena_usuario = models.CharField(max_length=30)

    tipo_usuario = models.ForeignKey(tipo_usuario, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)