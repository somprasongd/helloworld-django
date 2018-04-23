from django.urls import path, include
from rest_framework import routers
from upload_image.api.views import SimpleUploadedImagesViewSet, UploadedImagesViewSet

router = routers.DefaultRouter()
router.register('images_simple', SimpleUploadedImagesViewSet, 'images_simple')
router.register('images', UploadedImagesViewSet, 'images')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
