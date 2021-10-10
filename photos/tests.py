
from django.test import TestCase
from .models import Category,Photo,Location


# Create your tests here.
class PhotoTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.photo = Photo( description='my test')
        self.photo.save_photo()

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.photo,Photo))
    
        self.cat = Category(name="fashion")
        self.cat.save_category()

        self.loc = Location(name="Africa")
        self.loc.save_location()

        # Testing Save Method
    def test_save_method(self):
        self.photo.save_photo()
        images = Photo.objects.all()
        self.assertTrue(len(images) > 0)

    def tearDown(self):
        self.photo.delete_photo()
        