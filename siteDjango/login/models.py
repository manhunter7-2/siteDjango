from django.db import models
import hashlib as hash

# Create your models here.
class login(models.Model):
    email=models.EmailField()
    nickname=models.CharField(max_length=32)
    pwd=models.CharField(max_length=128)
