
from django.test import TestCase
from .models import Category,Photo,Location


# Create your tests here.

class LocationTestCLass(TestCase):
    #Set up Method
    def setUp(self):
        self.loc = Location(name="Africa")
        self.loc.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.loc,Location))

    def test_save_method(self):
        self.loc.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.loc.save_location()
        self.loc.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

class CategoryTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.cat = Category(name="fashion")
        self.cat.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))

    def test_save_method(self):
        self.cat.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

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
        