# Generated by Django 4.2.1 on 2024-02-29 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0033_audio_persona_audio_fisico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio_fono',
            name='otras_enfermedades',
        ),
    ]
