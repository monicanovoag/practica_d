# Generated by Django 4.2.1 on 2024-02-20 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0021_audio_fono_otras_enfermedades'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='audio_etiqueta',
            new_name='tipo_diagnostico_flgo',
        ),
        migrations.RenameField(
            model_name='audio_fono',
            old_name='audio_etiqueta',
            new_name='tipo_diagnostico_flgo',
        ),
        migrations.RenameField(
            model_name='audio_persona',
            old_name='audio_etiqueta',
            new_name='tipo_diagnostico_flgo',
        ),
    ]
