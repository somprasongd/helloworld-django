from rest_framework import serializers
# Import our UploadedImage model
from upload_image.models import SimpleUploadedImage


class SimpleUploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUploadedImage
        # only serialize the primary key and the image field
        fields = ('id', 'image', 'timestamp')
