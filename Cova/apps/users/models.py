# usuario/models.py
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_medical = models.BooleanField(default=False)
    
    is_patient = models.BooleanField(default=False)

    class Meta:
        db_table = 'users_db'

class MedicalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)
    num_coleg=models.CharField(max_length=64, default=0)


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)
    num_history=models.CharField(max_length=64, default=0)


