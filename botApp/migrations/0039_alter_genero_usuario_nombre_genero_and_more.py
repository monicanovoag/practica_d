# Generated by Django 4.2.1 on 2024-03-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0038_alter_otrasenf_nombre_otras_enf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero_usuario',
            name='nombre_genero',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='otrasenf',
            name='nombre_otras_enf',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tipo_diagnostico_flgo',
            name='nombre_diagnostico',
            field=models.CharField(max_length=100),
        ),
    ]