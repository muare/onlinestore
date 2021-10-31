from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=128,blank=False)
    location = models.CharField(max_length=128,blank=False)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128,blank=False)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE,related_name="products")
    description = models.TextField(max_length=1024,blank=True)
    photo = models.ImageField()
    price = models.FloatField(default=0)
    shipping_price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(blank=False)

    def __str__(self) -> str:
            return self.name
