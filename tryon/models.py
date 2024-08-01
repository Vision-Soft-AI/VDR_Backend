from django.db import models

# Create your models here.
class Shirt(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shirts/')

    def __str__(self):
        return self.name

class Pant(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pants/')

    def __str__(self):
        return self.name