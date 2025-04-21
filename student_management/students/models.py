# students/models.py
from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_no = models.CharField(max_length=15)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.student_name
