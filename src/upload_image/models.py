from django.db import models


# Our main model: Uploaded Image
class SimpleUploadedImage(models.Model):
    # stores the filename of an uploaded image
    image = models.ImageField("Uploaded image")
    timestamp = models.DateTimeField(auto_now_add=True)
