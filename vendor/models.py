from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)

def __str__(self):
        return self.name

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
