# Generated by Django 4.2.1 on 2024-02-19 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0016_alter_audio_etiqueta_nombre_etiqueta'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio_fono',
            name='otras_enfermedades',
            field=models.CharField(default=1, max_length=10, verbose_name='Otras Enf'),
            preserve_default=False,
        ),
    ]
