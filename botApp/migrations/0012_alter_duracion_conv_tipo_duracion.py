# Generated by Django 4.2.1 on 2024-03-12 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0011_duracion_conv_frecuencia_conv_funcion_conv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duracion_conv',
            name='tipo_duracion',
            field=models.CharField(choices=[('0-15 min', '0-15 min'), ('15-30 min', '15-30 min'), ('30-60 min', '30-60 min'), ('Más de 60 min', 'Más de 60 min')], max_length=20),
        ),
    ]