from rest_framework import viewsets
# import our serializer
from upload_image.api.serializers import SimpleUploadedImageSerializer
# import our model
from upload_image.models import SimpleUploadedImage


class UploadedImagesViewSet(viewsets.ModelViewSet):
    queryset = SimpleUploadedImage.objects.all()
    serializer_class = SimpleUploadedImageSerializer
