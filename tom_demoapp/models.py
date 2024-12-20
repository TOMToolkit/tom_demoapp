from django.db import models
from django.contrib.auth.models import User


class DemoProfile(models.Model):
    """Demo Profile model for a TOMToolkit User"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    demo_field = models.CharField(max_length=100, null=True, blank=True, verbose_name='Demo Field')
    demo_secret = models.CharField(max_length=100, null=True, blank=True, verbose_name='Demo Secret')

    def __str__(self):
        return f'{self.user.username} Demo App Profile'
