from django.contrib.auth.models import User
from django.db import models

from tom_common.encryption import EncryptedModelField


class DemoProfile(models.Model):
    """Demo Profile model for a TOMToolkit User."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    demo_field = models.CharField(max_length=100, null=True, blank=True, verbose_name='Demo Field')
    demo_secret = EncryptedModelField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user.username} Demo App Profile'
