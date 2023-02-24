from django.db import models

# Create your models here.
class register_tb(models.Model):
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)  
    confirmpassword=models.CharField(max_length=255)
