from django.db import models

# Create your models here.
from django.db import models

class Image(models.Model):
    
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =50)
    location = models.ForeignKey(location)
    category = models.ForeignKey(category)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']

class location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
