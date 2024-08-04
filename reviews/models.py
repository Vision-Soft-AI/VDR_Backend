from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.
class Reviews(models.Model):
    image = models.ImageField(upload_to='reviews_image/')
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    rating = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.name