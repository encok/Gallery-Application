
from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.cat = Category(name="fashion")
        self.cat.save_category()

        self.loc = Location(name="Africa")
        self.loc.save_location()
        # self.alabama= Image(name = 'Tour', description ='American Tour')
        self.alabama = Image(name='image test', description='my test',image_location=self.loc, image_category=self.cat)
        self.alabama.save_image()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.alabama,Image))

    # Testing Save Method
    def test_save_method(self):
        self.alabama.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    
    
    def tearDown(self):
        self.alabama.delete_image()
        self.cat.delete_category()
        self.loc.delete_location()

    def test_update_image(self):
        self.alabama.save_image()
        alabama = Image.update_image( self.alabama.id, 'test update', 'my test',self.loc, self.cat)
        upimage = Image.objects.filter(id = self.alabama.id)
        print(upimage)
        print(alabama)
        self.assertTrue(Image.name == 'test update')