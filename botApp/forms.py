from django import forms
from .models import *


class audio_fonoForm(forms.ModelForm):
    genero_usuario = forms.ModelChoiceField(
        queryset=genero_usuario.objects.all(),
        empty_label="Seleccione una opción",
    )

    audio_etiqueta = forms.ModelChoiceField(
        queryset=audio_etiqueta.objects.all(),
        empty_label="Seleccione una opción",
    )

    class Meta:
        model = audio_fono
        fields = ['id_paciente_ingresado','audio_fo','ano_nac','genero_usuario','audio_etiqueta','fecha_registro']

    def clean_genero_usuario(self):
        genero = self.cleaned_data['genero_usuario']
        return genero

    def clean_audio_etiqueta(self):
        audio_etiqueta = self.cleaned_data['audio_etiqueta']
        return audio_etiqueta       
