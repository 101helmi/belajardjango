from django.db import models
from .brandModel import Brand
from enum import Enum

class CategoryProduct(Enum):
    PARALLETTES = 'Paralleltes'
    ACCESSORIES = 'Accessories'

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=100,
        choices=[(status.value, status.name) for status in CategoryProduct],
        default=CategoryProduct.PARALLETTES.value,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_calisthenics'