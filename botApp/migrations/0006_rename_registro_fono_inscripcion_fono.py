# Generated by Django 4.2.1 on 2024-03-27 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0005_alter_registro_fono_telefono_fono'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='registro_fono',
            new_name='inscripcion_fono',
        ),
    ]
