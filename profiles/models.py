"""
Profile - name, email, bio
"""
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=250)
    email = models .EmailField(max_length=250, blank=True, null=True)
    bio = models. TextField(blank=True, null=True)

    def __str__(self):
        return self.name
