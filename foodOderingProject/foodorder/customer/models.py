from distutils.command.upload import upload
from unicodedata import category
from django.db import models

class MenuItem(models.Model):
    name =models.CharField(max_length=100)
    description= models.TextField()
    image = models.ImageField(upload_to= ' menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category= models.ManyToManyField('category', related_name= 'item')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


