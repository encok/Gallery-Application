from django.db import models

#location model
class Location(models.Model):
    name = models.CharField(max_length =50)
    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

  
#category model
class Category(models.Model):
    name = models.CharField(max_length =50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()



#image model
class Image(models.Model):
    name = models.CharField(max_length = 60)
    description = models.TextField()
    image_location = models.ForeignKey('Location' ,on_delete=models.CASCADE, null=True)
    image_category = models.ForeignKey('Category' ,on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['name']

    @classmethod
    def update_image(cls, id ,name, description , image_location, image_category):
        update = cls.objects.filter(id = id).update(name = name, description = description ,image_location = image_location,image_category = image_category)
        return update

    