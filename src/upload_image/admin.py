from django.contrib import admin
from upload_image.models import SimpleUploadedImage, UploadedImage

# Register your models here.
admin.site.register(SimpleUploadedImage)
admin.site.register(UploadedImage)
