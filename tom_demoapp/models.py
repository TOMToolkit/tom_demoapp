from django.db import models
from django.contrib.auth.models import User
from tom_common.models import EncryptedProperty


class DemoProfile(models.Model):
    """Demo Profile model for a TOMToolkit User"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    demo_field = models.CharField(max_length=100, null=True, blank=True, verbose_name='Demo Field')
    _demo_secret_encrypted = models.BinaryField(null=True, blank=True)  # ciphertext (private)
    demo_secret = EncryptedProperty('_demo_secret_encrypted')               # descriptor (public)

    def __str__(self):
        return f'{self.user.username} Demo App Profile'
