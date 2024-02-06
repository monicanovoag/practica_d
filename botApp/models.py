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
    
class audio_persona(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_audio") 
    audio_us = models.FileField(upload_to='audios/')
    wsp_usuario = models.IntegerField()
    ano_nac = models.CharField(max_length=10, verbose_name="año_nacimiento")
    fecha_ingreso_persona = models.DateTimeField(default=timezone.now)

    genero_usuario = models.ForeignKey(genero_usuario, on_delete=models.CASCADE)
    audio_etiqueta = models.ForeignKey(audio_etiqueta, on_delete=models.CASCADE)

class audio_fono(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_audio") 
    audio_fo = models.FileField(upload_to='audios/')
    ano_nac = models.CharField(max_length=10, verbose_name="año_nacimiento")
    fecha_ingreso_fono = models.DateTimeField(default=timezone.now)

    genero_usuario = models.ForeignKey(genero_usuario, on_delete=models.CASCADE)
    audio_etiqueta = models.ForeignKey(audio_etiqueta, on_delete=models.CASCADE)

class usuario (models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_usuario")
    nombre_usuario = models.CharField(max_length=20)
    apellido_usuario = models.CharField(max_length=20)
    correo_usuario = models.EmailField(max_length=40)
    tipo_usuario = models.CharField(max_length=20)

    audio_persona = models.ForeignKey(audio_persona, on_delete=models.CASCADE)
    audio_fono = models.ForeignKey(audio_fono, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)