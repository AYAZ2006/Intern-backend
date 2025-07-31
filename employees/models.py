from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    doj = models.DateField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
