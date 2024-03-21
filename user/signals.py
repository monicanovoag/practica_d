from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from .models import Log

@receiver(user_logged_in)
def handle_login(sender, request, user, **kwargs):
    Log.objects.create(username=user.username)