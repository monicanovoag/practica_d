# Generated by Django 4.2.1 on 2024-02-28 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botApp', '0031_alter_audio_persona_wsp_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio_persona',
            old_name='audio_usuario',
            new_name='audio_manychat',
        ),
    ]
