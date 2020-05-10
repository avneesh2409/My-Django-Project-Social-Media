from django.db import models
# Create your models here.
# models.py
#from django.db import models
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

import datetime
class Student(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    education = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    date = models.DateField(default = datetime.datetime.now())

    def __str__(self):
        return self.name + self.date