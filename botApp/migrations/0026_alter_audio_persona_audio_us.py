# Generated by Django 4.2.1 on 2024-02-27 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0025_audio_persona_comuna_residencia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_persona',
            name='audio_us',
            field=models.FileField(upload_to='audios/personas/'),
        ),
    ]