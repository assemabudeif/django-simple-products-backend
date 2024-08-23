from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# class Users(models.Model):
#     username = models.CharField(max_length=50, primary_key=True)
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name