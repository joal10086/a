# models.py
from django.db import models
 
class Test(models.Model):
    name = models.CharField(max_length=20)
    
class customers(models.Model):
    class Meta:
        db_table='customers'
    id = models.AutoField
    loginname = models.CharField(max_length=16)