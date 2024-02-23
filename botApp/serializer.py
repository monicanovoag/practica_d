from rest_framework import serializers
from .models import *

class audio_fonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = audio_fono
        fields = "__all__"

class audio_personaSerializer(serializers.ModelSerializer):
    class Meta:
        model = audio_persona
        fields = "__all__"