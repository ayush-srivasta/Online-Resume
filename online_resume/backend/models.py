from distutils.command.upload import upload
from django.db import models

from user.models import ResumeUser
from django.contrib.auth.models import User

# Create your models here.
class Resume(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to="image",blank=True,null=True)
    file=models.FileField(upload_to='pdf')
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)

    def __str__(self):
        return self.user.username+" "+self.name