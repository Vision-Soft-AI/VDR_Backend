from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    company = models.CharField(max_length=255)
    description = models.TextField(
        max_length=500, 
        blank=True)

    def __str__(self):
        return self.company