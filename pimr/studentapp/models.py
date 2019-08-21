from django.db import models

class Student(models.Model):
    rno = models.CharField(max_length=200)
    sname = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    fees = models.IntegerField()
    def __str__(self):
    	return "Rno is "+self.rno+" Name is "+self.sname+" branch is "+self.branch+ "Fees is "+str(self.fees)

class Reg(models.Model):
   email=models.CharField(max_length=50)
   passsword=models.CharField(max_length=10)
   mobileno=models.CharField(max_length=12)
   fullname=models.CharField(max_length=50)
   def __str__(self):
    	return "Email is "+self.email+" passsword is "+self.passsword+" mobileno is "+self.mobileno+ "fullname is "+self.fullname

