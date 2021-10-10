import cloudinary
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def test_delete_method(self):
        self.cat.save_category()
        self.cat.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

class Location(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def test_delete_method(self):
        self.loc.save_location()
        self.loc.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.description

    
    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()