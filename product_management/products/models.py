# products/models.py
from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.product_name
