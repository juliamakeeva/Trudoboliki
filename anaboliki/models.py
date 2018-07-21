from django.db import models


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

    def __str__(self):
        return self.name