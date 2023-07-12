from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to="image")

