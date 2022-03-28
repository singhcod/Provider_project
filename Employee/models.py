from django.db import models
from django.urls import reverse

# Create your models here.
class Employees(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    address = models.CharField(max_length=270)
    mobile  = models.BigIntegerField( unique=True)

    def __str__(self):
        return self.ename


    def get_absolute_url(self):
        return reverse("employeelist")



