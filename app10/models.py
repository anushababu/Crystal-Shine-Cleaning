from django.db import models

# Create your models here.
class register_tb(models.Model):
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)  
    confirmpassword=models.CharField(max_length=255)

class category_tb(models.Model):
    category=models.CharField(max_length=255)
    image=models.ImageField(upload_to="product/")

class service_tb(models.Model):
	servicename=models.CharField(max_length=255)
	category=models.ForeignKey(category_tb,on_delete=models.CASCADE)
	price=models.CharField(max_length=255)
	desc=models.TextField()
	image=models.ImageField(upload_to="product/") 

class gallery_tb(models.Model):
    image=models.ImageField(upload_to="product/")

class contactf_tb(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)  
    subject=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    message=models.TextField()           


#####################################################admin########################################################################    		    


class getin_tb(models.Model):
    serid=models.ForeignKey(service_tb, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)  
    phone=models.CharField(max_length=255)
    address=models.CharField(max_length=255)

class team_tb(models.Model):
    image=models.ImageField(upload_to="product/")
    name=models.CharField(max_length=255)  
    desc=models.CharField(max_length=255)
    contact=models.CharField(max_length=255)    
    