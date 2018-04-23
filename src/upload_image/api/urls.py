from django.urls import path, include
from rest_framework import routers
from upload_image.api.views import UploadedImagesViewSet

router = routers.DefaultRouter()
router.register('images_simple', UploadedImagesViewSet, 'images_simple')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
