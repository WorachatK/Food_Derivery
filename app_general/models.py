from pickle import TRUE
from telnetlib import AUTHENTICATION
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class type_food(models.Model):
    type = models.CharField(max_length=40)

    def __str__(self):
        return self.type

class food(models.Model):
    name = models.CharField(max_length=40)
    type = models.ForeignKey(type_food, on_delete=models.CASCADE)
    price = models.IntegerField()
    photo = models.CharField(max_length=60,null=TRUE)
    descriptiob = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Food"
        verbose_name = "food"

    def __str__(self):
        return self.name

class order_food(models.Model):
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    phonenumber = models.CharField(max_length=10,null=True)
    address = models.TextField(null=True)

class check_food(models.Model):
    username = models.CharField(max_length=40)
    food =  models.ForeignKey(food, on_delete=models.CASCADE)
    time = models.DateField(null=True)
