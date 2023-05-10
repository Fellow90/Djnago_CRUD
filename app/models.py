from statistics import mode
from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=25,null=True)
    email=models.CharField(max_length=25,null=True)
    password=models.CharField(max_length=16,null=True)

    def __str__(self):
        return self.name