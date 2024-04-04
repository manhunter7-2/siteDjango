from django.db import models

# Create your models here.
class login(models.Model):
    name=models.CharField(max_length=32)
    pwd=models.IntegerField()
