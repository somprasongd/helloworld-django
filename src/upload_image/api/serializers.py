from rest_framework import serializers
# Import our UploadedImage model
from upload_image.models import SimpleUploadedImage, UploadedImage


class SimpleUploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUploadedImage
        # only serialize the primary key and the image field
        fields = ('id', 'image', 'timestamp')


class UploadedImageSerializer(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides the pk, image, thumbnail, title and description
    """
    class Meta:
        model = UploadedImage
        fields = ('id', 'image', 'thumbnail', 'title', 'description', 'timestamp')
        read_only_fields = ('thumbnail',)
