# employees/models.py
from django.db import models

class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_no = models.CharField(max_length=15)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.employee_name
