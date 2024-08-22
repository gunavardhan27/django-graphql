from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserRole(models.Model):
    role = models.CharField(max_length=100)
    def __str__(self):
        return self.role
class User(AbstractUser):
    username = models.CharField(max_length=200,blank=True,unique=True)
    role = models.ForeignKey(UserRole,on_delete=models.CASCADE,blank=True,null=True,default=2)
    email = models.CharField(max_length=200,blank=True,unique=True)
    firstname = models.CharField(max_length=60,default='Uninitialised')
    lastname = models.CharField(max_length=60,default='User')
    phone = models.CharField(max_length=20, blank=True)
    googleLogin=models.BooleanField(default="False")
    manualLogin = models.BooleanField(default="False")
    def  __str__(self):
        return self.username
    
class Post(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(max_length=400)
    def __str__(self):
        return self.title
    
