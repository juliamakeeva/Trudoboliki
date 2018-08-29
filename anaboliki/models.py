from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    adress = models.TextField()
    tel = models.DecimalField(max_digits=15, decimal_places=0)
    cities = models.ForeignKey(
        'City',
        on_delete=models.CASCADE,)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,
                             null=True, blank=True,
                             on_delete=models.SET_NULL)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


#class User(models.Model):
    #username = models.CharField(max_length=100)
    #email = models.EmailField(max_length=100)
    #password1 = models.CharField(max_length=100)
    #password2 = models.CharField(max_length=100)

    #def __str__(self):
       # return self.name