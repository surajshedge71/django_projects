from django.db import models

class Customer(models.Model):
    cname = models.CharField(max_length=20)
    sales = models.IntegerField()

    def __str__(self):
        return self.cname

class Emp(Customer):
    ename = models.CharField(max_length=20)
    sal = models.IntegerField()

    def __str__(self):
        return self.ename

class Student(Emp):
    sname = models.CharField(max_length=20)
    marks = models.IntegerField()

    def __str__(self):
        return self.sname





# Create your models here.
