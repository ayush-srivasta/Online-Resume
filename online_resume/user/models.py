from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.contrib.auth.models import User
# Create yor models here.


class ResumeUser(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author
