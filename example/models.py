from django.db import models

from framework.base_entity import BaseEntity

# Create your models here.
class ProductExample(models.Model, BaseEntity):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
