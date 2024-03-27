from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.


class tipo_diagnostico_flgo(models.Model):


    id = models.AutoField(primary_key=True, verbose_name="id_etiqueta") 
    nombre_diagnostico = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_diagnostico
    

class genero_usuario(models.Model):
    
    id = models.AutoField(primary_key=True, verbose_name="id_genero") 
    nombre_genero = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre_genero
    
class OtrasEnf(models.Model):

    nombre_otras_enf = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_otras_enf
    

class sistema_salud(models.Model):
    
    id = models.AutoField(primary_key=True, verbose_name="id_sistema") 
    nombre_sistema = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre_sistema
    

class audio_persona(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_audio")
    wsp_usuario = models.CharField(max_length = 30) 
    ano_nac = models.CharField(max_length=10, verbose_name="año_nacimiento")
    comuna_usuario = models.CharField(max_length=30, verbose_name="comuna")
    audio_manychat = models.CharField(max_length=255)     
    fecha_registro_paciente = models.DateTimeField(default=timezone.now)

    genero_usuario = models.ForeignKey(genero_usuario, on_delete=models.CASCADE)  
    sistema_salud = models.ForeignKey(sistema_salud, on_delete=models.CASCADE)  

    # Otros campos del modelo
    audio_fisico = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.audio_manychat and not self.audio_fisico:
            self.audio_fisico = self.audio_manychat
        super().save(*args, **kwargs)
       

class audio_fono(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_audio") 
    id_usuario = models.CharField(max_length = 30) 
    nombre_paciente = models.CharField(max_length=20)
    audio_fo1 = models.FileField(upload_to='audios/fono/')
    audio_fo2 = models.FileField(upload_to='audios/fono/', blank=True, null=True)
    audio_fo3 = models.FileField(upload_to='audios/fono/', blank=True, null=True)
    audio_fo4 = models.FileField(upload_to='audios/fono/', blank=True, null=True)
    audio_fo5 = models.FileField(upload_to='audios/fono/', blank=True, null=True)
    ano_nac = models.CharField(max_length=10, verbose_name="Año Nacimiento")
    fecha_registro = models.DateTimeField(default=timezone.now)

    genero_usuario = models.ForeignKey(genero_usuario, on_delete=models.CASCADE)
    tipo_diagnostico_flgo = models.ForeignKey(tipo_diagnostico_flgo, on_delete=models.CASCADE)
    otras_enf = models.ManyToManyField(OtrasEnf)
        
#CLASES PARA FORMULARIO SOCIOCOMUNICATIVO 
    
class tipo_relacion(models.Model):

    CONYUGE = "Conyuge"
    HIJO_A = "Hijo o Hija"
    OTRO_FAMILIAR = "Otros familiares"
    OTRA_PERSONA = "Otras personas"

    RELACION_CHOICES = [
        (CONYUGE, "Conyuge"),
        (HIJO_A, "Hijo o Hija"),
        (OTRO_FAMILIAR, "Otros familiares"),
        (OTRA_PERSONA,"Otras personas"),]

    id = models.AutoField(primary_key=True, verbose_name="id_relacion")
    tipo_relacion = models.CharField(max_length=30, choices=RELACION_CHOICES)

    def __str__(self):
        return self.tipo_relacion
    
class frecuencia_conv(models.Model):

    ESPORADICA = "Esporadica"
    MENSUAL = "Mensual"
    SEMANAL = "Semanal"
    DIARIA = "Diaria"
    VARIAS_VECES_DIA = "Varias veces al día"

    FRECUENCIA_CHOICES = [
        (ESPORADICA, "Esporadica"),
        (MENSUAL, "Mensual"),
        (SEMANAL, "Semanal"),
        (DIARIA, "Diaria"),
        (VARIAS_VECES_DIA, "Varias veces al día"),]

    id = models.AutoField(primary_key=True, verbose_name="id_frecuencia")
    tipo_frecuencia = models.CharField(max_length=20, choices=FRECUENCIA_CHOICES)

    def __str__(self):
        return self.tipo_frecuencia
    
class duracion_conv(models.Model):

    MIN_0_15 = "0-15 min"
    MIN_15_30 = "15-30 min"
    MIN_30_60 = "30-60 min"
    MIN_60_MAS = "Más de 60 min"


    DURACION_CHOICES = [
        (MIN_0_15, "0-15 min"),
        (MIN_15_30, "15-30 min"),
        (MIN_30_60, "30-60 min"),
        (MIN_60_MAS, "Más de 60 min"),]

    id = models.AutoField(primary_key=True, verbose_name="id_duracion")
    tipo_duracion = models.CharField(max_length=20, choices=DURACION_CHOICES)  


    def __str__(self):
        return self.tipo_duracion

class funcion_conv(models.Model):

    SATISFACCION = "Satisfacción de las necesidades vitales"
    EMOCIONES = "Emociones o propósito en la vida"
    NOTICIAS = "Noticias o información mundial"
    OTRO = "Otro"


    FUNCION_CHOICES = [
        (SATISFACCION, "Satisfacción de las necesidades vitales"),
        (EMOCIONES, "Emociones o propósito en la vida"),
        (NOTICIAS, "Noticias o información mundial"),
        (OTRO, "Otro"),]

    id = models.AutoField(primary_key=True, verbose_name="id_duracion")
    tipo_funcion = models.CharField(max_length=100, choices=FUNCION_CHOICES)  

    def __str__(self):
        return self.tipo_funcion
    
class satisfaccion_conv(models.Model):

    NADA = "Nada satisfecho"
    POCO = "Poco satisfecho"
    MEDIANAMENTE = "Medianamente satisfecho"
    SATISFECHO = "Satisfecho"
    MUY_SATISFECHO = "Muy satisfecho"


    SATISFACCIONES_CHOICES = [
        (NADA, "Nada satisfecho"),
        (POCO, "Poco satisfecho"),
        (MEDIANAMENTE, "Medianamente satisfecho"),
        (SATISFECHO, "Satisfecho"),
        (MUY_SATISFECHO, "Muy satisfecho"),]

    id = models.AutoField(primary_key=True, verbose_name="id_duracion")
    tipo_satisfaccion = models.CharField(max_length=100, choices=SATISFACCIONES_CHOICES)  

    def __str__(self):
        return self.tipo_satisfaccion
    
    
class formulario_com(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id_formulario") 
    id_fono = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    ano_nac = models.CharField(max_length=10, verbose_name="año Nacimiento")
    fecha_ingreso = models.DateTimeField(default=timezone.now)

    genero_usuario = models.ForeignKey(genero_usuario, on_delete=models.CASCADE)

    #----------------------RESPUESTAS FORMULARIO-----------------------

    #RELACIÓN CON EL PACIENTE 
    tipo_relacion_1 = models.ForeignKey(tipo_relacion, related_name='formulario_com_1', verbose_name="tipo_relacion_1", on_delete=models.CASCADE, null=True, blank=True)
    tipo_relacion_2 = models.ForeignKey(tipo_relacion, related_name='formulario_com_2', verbose_name="tipo_relacion_2", on_delete=models.CASCADE, null=True, blank=True)
    tipo_relacion_3 = models.ForeignKey(tipo_relacion, related_name='formulario_com_3', verbose_name="tipo_relacion_3", on_delete=models.CASCADE, null=True, blank=True)
    tipo_relacion_4 = models.ForeignKey(tipo_relacion, related_name='formulario_com_4', verbose_name="tipo_relacion_4", on_delete=models.CASCADE, null=True, blank=True)

    #FRECUENCIA 
    frecuencia_1 = models.ForeignKey(frecuencia_conv, related_name='formulario_com_1', verbose_name="frecuencia_1", on_delete=models.CASCADE, null=True, blank=True)
    frecuencia_2 = models.ForeignKey(frecuencia_conv, related_name='formulario_com_2', verbose_name="frecuencia_2", on_delete=models.CASCADE, null=True, blank=True)
    frecuencia_3 = models.ForeignKey(frecuencia_conv, related_name='formulario_com_3', verbose_name="frecuencia_3", on_delete=models.CASCADE, null=True, blank=True)
    frecuencia_4 = models.ForeignKey(frecuencia_conv, related_name='formulario_com_4', verbose_name="frecuencia_4", on_delete=models.CASCADE, null=True, blank=True)

    #DURACIÓN 
    duracion_1 = models.ForeignKey(duracion_conv, related_name='formulario_com_1', verbose_name="duracion_1", on_delete=models.CASCADE, null=True, blank=True)
    duracion_2 = models.ForeignKey(duracion_conv, related_name='formulario_com_2', verbose_name="duracion_2", on_delete=models.CASCADE, null=True, blank=True)
    duracion_3 = models.ForeignKey(duracion_conv, related_name='formulario_com_3', verbose_name="duracion_3", on_delete=models.CASCADE, null=True, blank=True)
    duracion_4 = models.ForeignKey(duracion_conv, related_name='formulario_com_4', verbose_name="duracion_4", on_delete=models.CASCADE, null=True, blank=True)

    #FUNCION 
    funcion_1 = models.ForeignKey(funcion_conv, related_name='formulario_com_1', verbose_name="funcion_1", on_delete=models.CASCADE, null=True, blank=True)
    funcion_2 = models.ForeignKey(funcion_conv, related_name='formulario_com_2', verbose_name="funcion_2", on_delete=models.CASCADE, null=True, blank=True)
    funcion_3 = models.ForeignKey(funcion_conv, related_name='formulario_com_3', verbose_name="funcion_3", on_delete=models.CASCADE, null=True, blank=True)
    funcion_4 = models.ForeignKey(funcion_conv, related_name='formulario_com_4', verbose_name="funcion_4", on_delete=models.CASCADE, null=True, blank=True)

    #SATISFACCIÓN
    satisfaccion_1 = models.ForeignKey(satisfaccion_conv, related_name='formulario_com_1', verbose_name="satisfaccion_1", on_delete=models.CASCADE, null=True, blank=True)
    satisfaccion_2 = models.ForeignKey(satisfaccion_conv, related_name='formulario_com_2', verbose_name="satisfaccion_2", on_delete=models.CASCADE, null=True, blank=True)
    satisfaccion_3 = models.ForeignKey(satisfaccion_conv, related_name='formulario_com_3', verbose_name="satisfaccion_3", on_delete=models.CASCADE, null=True, blank=True)
    satisfaccion_4 = models.ForeignKey(satisfaccion_conv, related_name='formulario_com_4', verbose_name="satisfaccion_4", on_delete=models.CASCADE, null=True, blank=True)

    #COMPLEMENTO 
    complemento_1 = models.CharField(max_length=2000, null=True, blank=True)
    complemento_2 = models.CharField(max_length=2000, null=True, blank=True)
    complemento_3 = models.CharField(max_length=2000, null=True, blank=True)
    complemento_4 = models.CharField(max_length=2000, null=True, blank=True)


    def __str__(self):
        return str(self.id)
    

class inscripcion_fono(models.Model):
    nombre_fono = models.CharField(max_length=100)
    apellido_fono = models.CharField(max_length=100)
    email_fono = models.EmailField()
    telefono_fono = models.IntegerField()
    comuna_residencia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_fono
    
