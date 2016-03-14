# usuario/models.py
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models



class UserManager(BaseUserManager, models.Manager):

    def _create_user(self,username, email, password, is_staff,
                     is_superuser, **extra_fields):
        email=self.normalize_email(email)
        if not email:
            raise ValueError('El email debe ser obligatorio')
        user=self.model(username=username, email=email, is_active=True, is_staff=is_staff
                   ,**extra_fields )

        user.setpassword(password)
        user.save(using=self._db)
        return user

    def create_user(self,username,email,password=None,**extra_fields):
        return self._create_user(username,email,password, False,False,**extra_fields)

    def create_user(self,username,email,password=None,**extra_fields):
        return self._create_user(username,email,password, True,True,**extra_fields)

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


