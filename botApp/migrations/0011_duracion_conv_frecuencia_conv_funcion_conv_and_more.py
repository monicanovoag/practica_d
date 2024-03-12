# Generated by Django 4.2.1 on 2024-03-12 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0010_alter_audio_persona_audio_fisico'),
    ]

    operations = [
        migrations.CreateModel(
            name='duracion_conv',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id_duracion')),
                ('tipo_duracion', models.CharField(choices=[('0-15 min', 'Esporadica'), ('15-30 min', 'Mensual'), ('30-60 min', 'Semanal'), ('Más de 60 min', 'Diaria')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='frecuencia_conv',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id_frecuencia')),
                ('tipo_frecuencia', models.CharField(choices=[('Esporadica', 'Esporadica'), ('Mensual', 'Mensual'), ('Semanal', 'Semanal'), ('Diaria', 'Diaria'), ('Varias veces al día', 'Varias veces al día')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='funcion_conv',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id_duracion')),
                ('tipo_funcion', models.CharField(choices=[('Satisfacción de las necesidades vitales', 'Satisfacción de las necesidades vitales'), ('Emociones o propósito en la vida', 'Emociones o propósito en la vida'), ('Noticias o información mundial', 'Noticias o información mundial'), ('Otro', 'Otro')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='satisfaccion_conv',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id_duracion')),
                ('tipo_satisfaccion', models.CharField(choices=[('Nada satisfecho', 'Nada satisfecho'), ('Poco satisfecho', 'Poco satisfecho'), ('Medianamente satisfecho', 'Medianamente satisfecho'), ('Satisfecho', 'Satisfecho'), ('Muy satisfecho', 'Muy satisfecho')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_relacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id_relacion')),
                ('tipo_relacion', models.CharField(choices=[('Conyuge', 'Conyuge'), ('Hijo o Hija', 'Hijo o Hija'), ('Otros familiares', 'Otros familiares'), ('Otras personas', 'Otras personas')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='formulario_com',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id_formulario')),
                ('nombre', models.CharField(max_length=20)),
                ('ano_nac', models.CharField(max_length=10, verbose_name='año Nacimiento')),
                ('complementos', models.CharField(max_length=1000)),
                ('duracion_conv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botApp.duracion_conv')),
                ('frecuencia_conv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botApp.frecuencia_conv')),
                ('funcion_conv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botApp.funcion_conv')),
                ('genero_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botApp.genero_usuario')),
                ('satisfaccion_conv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botApp.satisfaccion_conv')),
                ('tipo_relacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botApp.tipo_relacion')),
            ],
        ),
    ]
