from rest_framework import viewsets
# import our serializer
from upload_image.api.serializers import SimpleUploadedImageSerializer, UploadedImageSerializer
# import our model
from upload_image.models import SimpleUploadedImage, UploadedImage


class SimpleUploadedImagesViewSet(viewsets.ModelViewSet):
    queryset = SimpleUploadedImage.objects.all()
    serializer_class = SimpleUploadedImageSerializer


class UploadedImagesViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer
