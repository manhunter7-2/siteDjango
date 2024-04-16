from django.db import models
from customExceptions.models import CustomException as cExept

# Create your models here.
class Login(models.Model):
    email=models.EmailField()
    nickname=models.CharField(max_length=32)
    pwd=models.CharField(max_length=128)
    exception=cExept
