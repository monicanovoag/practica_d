# Generated by Django 4.2.1 on 2024-03-01 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0037_alter_genero_usuario_nombre_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otrasenf',
            name='nombre_otras_enf',
            field=models.CharField(max_length=30),
        ),
    ]
