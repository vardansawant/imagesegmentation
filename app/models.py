from django.db import models

# Create your models here.
class ImageModel(models.Model):
    image_name = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to='input/')