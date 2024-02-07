# Generated by Django 4.2.1 on 2024-02-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("botApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="tipo_usuario",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="id_tipo_usuario",
                    ),
                ),
                (
                    "nombre_tipo_usuario",
                    models.CharField(
                        choices=[
                            ("Usuario", "Usuario"),
                            ("Paciente", "Paciente"),
                            ("admin", "Admin"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="audio_fono",
            name="fecha_ingreso_fono",
        ),
        migrations.RemoveField(
            model_name="audio_persona",
            name="fecha_ingreso_persona",
        ),
        migrations.AddField(
            model_name="audio_fono",
            name="fecha_registro",
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="audio_persona",
            name="fecha_registro_paciente",
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]