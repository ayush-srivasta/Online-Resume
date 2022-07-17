from distutils.command.upload import upload
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from user.models import ResumeUser
from django.contrib.auth.models import User

# Create your models here.
class Resume(models.Model):
    name=models.CharField(max_length=255,unique=True)
    image=models.ImageField(upload_to="image",blank=True,null=True)
    file=models.FileField(upload_to='pdf',blank=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)

    def __str__(self):
        return self.user.username+" "+self.name
    
    
@receiver(pre_delete, sender=Resume)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)
    