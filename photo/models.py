from django.db import models

# Create your models here.
from django.db import models

class Image(models.Model):
    image = models.CharField(max_length =30)
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =50)
    
    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
