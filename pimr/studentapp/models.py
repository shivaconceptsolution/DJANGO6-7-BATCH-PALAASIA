from django.db import models

class Student(models.Model):
    rno = models.CharField(max_length=200)
    sname = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    fees = models.IntegerField()
