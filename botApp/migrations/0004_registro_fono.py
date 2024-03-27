# Generated by Django 4.2.1 on 2024-03-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0003_alter_audio_fono_id_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='registro_fono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_fono', models.CharField(max_length=100)),
                ('apellido_fono', models.CharField(max_length=100)),
                ('email_fono', models.EmailField(max_length=254)),
                ('telefono_fono', models.IntegerField(max_length=9)),
                ('comuna_residencia', models.CharField(max_length=100)),
            ],
        ),
    ]
