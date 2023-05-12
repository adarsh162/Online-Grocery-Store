from distutils.command.upload import upload
from unicodedata import category

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class products(models.Model):
  #  id : int
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pic')
    price = models.IntegerField()
   
    offer = models.BooleanField(default=False)
    oldp = models.IntegerField()
    


