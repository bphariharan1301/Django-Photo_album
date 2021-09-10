from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Upload(models.Model):
    title = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='images/')
    image = CloudinaryField()

    def __str__(self):
        return self.title
