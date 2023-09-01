from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50,null=bool)
    
