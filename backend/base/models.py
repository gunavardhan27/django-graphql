from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=200,blank=True,unique=True)
    email = models.CharField(max_length=200,blank=True,unique=True)
    firstname = models.CharField(max_length=60,default='Uninitialised')
    lastname = models.CharField(max_length=60,default='User')
    phone = models.CharField(max_length=20, blank=True)
    googleLogin=models.BooleanField(default="False")
    manualLogin = models.BooleanField(default="False")
    def  __str__(self):
        return self.username