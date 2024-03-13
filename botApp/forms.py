from django import forms
from .models import *


class audio_fonoForm(forms.ModelForm):

    otras_enf = forms.ModelMultipleChoiceField(queryset=OtrasEnf.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    
    class Meta:
        model = audio_fono
        fields = ['audio_fo1','audio_fo2','audio_fo3','audio_fo4','audio_fo5','ano_nac','genero_usuario','tipo_diagnostico_flgo','nombre_paciente','otras_enf']

    def clean_genero_usuario(self):
        genero = self.cleaned_data['genero_usuario']
        return genero

    def clean_tipo_diagnostico_flgo(self):
        tipo_diagnostico_flgo = self.cleaned_data['tipo_diagnostico_flgo']
        return tipo_diagnostico_flgo

    def clean_audio_fo(self):
        audio_file = self.cleaned_data.get('audio_fo1', False)
        if audio_file:
            if not audio_file.name.endswith(('.mp3', '.wav', '.ogg', '.flac', '.aac','.opus')):
                raise forms.ValidationError('Por favor, suba un archivo de audio válido (MP3, WAV, OGG, FLAC, AAC).')
        return audio_file
    
    def clean(self):
        cleaned_data = super().clean()
        audio_files = [
            cleaned_data.get('audio_fo1'),
            cleaned_data.get('audio_fo2'),
            cleaned_data.get('audio_fo3'),
            cleaned_data.get('audio_fo4'),
            cleaned_data.get('audio_fo5'),
        ]
        if not any(audio_files):
            raise forms.ValidationError('Debe subir al menos un archivo de audio.')
        return cleaned_data
    
class formulario_comunicacion(forms.ModelForm):

    class Meta:
        model = formulario_com
        fields = "__all__"


class respuestas_formulario(forms.ModelForm):
    
    class Meta:
        model = respuestas_form
        fields = ['tipo_relacion','frecuencia_conv','duracion_conv','funcion_conv','satisfaccion_conv','complementos']

        widgets = {
            'complementos': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }