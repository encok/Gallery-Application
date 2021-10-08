from django.db import models

#location model
class Location(models.Model):
    name = models.CharField(max_length =50)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

#category model
class Category(models.Model):
    name = models.CharField(max_length =50)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']