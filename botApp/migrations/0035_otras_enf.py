# Generated by Django 4.2.1 on 2024-02-29 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0034_remove_audio_fono_otras_enfermedades'),
    ]

    operations = [
        migrations.CreateModel(
            name='otras_enf',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id_otrasEnf')),
                ('nombre_otrasEnf', models.CharField(choices=[('Enfermedad de Parkinson', 'Enfermedad de Parkinson'), ('Diabetes', 'Diabetes'), ('Hipertensión', 'Hipertensión'), ('Ninguna', 'Ninguna')], max_length=30)),
            ],
        ),
    ]
