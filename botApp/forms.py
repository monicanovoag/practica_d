from django import forms
from .models import *


class audio_fonoForm(forms.ModelForm):
    
    ENFERMEDADES_CHOICES = [
        ('parkinson', 'Enfermedad de Parkinson'),
        ('diabetes', 'Diabetes'),
        ('hipertension', 'Hipertensión'),
    ]

    otras_enfermedades = forms.MultipleChoiceField(
        choices=ENFERMEDADES_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    class Meta:
        model = audio_fono
        fields = ['audio_fo','audio_fo2','audio_fo3','audio_fo4','audio_fo5','ano_nac','genero_usuario','audio_etiqueta','nombre_paciente','otras_enfermedades']


    def clean_genero_usuario(self):
        genero = self.cleaned_data['genero_usuario']
        return genero

    def clean_audio_etiqueta(self):
        audio_etiqueta = self.cleaned_data['audio_etiqueta']
        return audio_etiqueta

    def clean_audio_fo(self):
        audio_file = self.cleaned_data.get('audio_fo', False)
        if audio_file:
            if not audio_file.name.endswith(('.mp3', '.wav', '.ogg', '.flac', '.aac')):
                raise forms.ValidationError('Por favor, suba un archivo de audio válido (MP3, WAV, OGG, FLAC, AAC).')
        return audio_file
    
    def clean(self):
        cleaned_data = super().clean()
        audio_files = [
            cleaned_data.get('audio_fo'),
            cleaned_data.get('audio_fo2'),
            cleaned_data.get('audio_fo3'),
            cleaned_data.get('audio_fo4'),
            cleaned_data.get('audio_fo5'),
        ]
        if not any(audio_files):
            raise forms.ValidationError('Debe subir al menos un archivo de audio.')
        return cleaned_data