from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Prace', decimal_places=2, max_digits=8)
    quantity = models.IntegerField('Quantity')

    def __str__(self):
        return self.name
class Client(models.Model):
    name = models.CharField('Name', max_length=100)
    lastname = models.CharField('Last name', max_length=100)
    email = models.EmailField('Email', max_length=100)

    def __str__(self):
        return f'{self.name} {self.lastname}'