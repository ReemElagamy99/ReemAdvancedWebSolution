from django.db import models

#beykteb feeh l details l btro7 3al database

# Create your models here.

from django.db import models

#da mogarad gadwal lesa mat7atesh fel database
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)

