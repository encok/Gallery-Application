
from django.test import TestCase
from .models import Category,Photo,Location


# Create your tests here.
class PhotoTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.photo= Photo(description ='Photo of my wife and i  in mount Albert in Colorado')

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.photo,Photo))

        # Testing Save Method
    def test_save_method(self):
        self.photo.save_photo()
        images = Photo.objects.all()
        self.assertTrue(len(images) > 0)