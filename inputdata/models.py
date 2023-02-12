from django.db import models

class data (models.Model):
    name=models.CharField(max_length=20)
    mobno=models.CharField(max_length=10)
    city=models.CharField(max_length=50)
    
# Create your models here.
