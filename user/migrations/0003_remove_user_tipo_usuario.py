# Generated by Django 4.2.1 on 2024-03-20 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_tipo_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tipo_usuario',
        ),
    ]
