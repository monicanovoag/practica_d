# Generated by Django 4.2.1 on 2024-02-27 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0026_alter_audio_persona_audio_us'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio_persona',
            name='tipo_diagnostico_flgo',
        ),
    ]