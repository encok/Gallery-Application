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


#image model
class Image(models.Model):
    name = models.CharField(max_length = 60)
    description = models.TextField()
    image_location = models.ForeignKey('Location')
    image_category = models.ForeignKey('Category')