# Upload Image
ตัวอย่าง ทำ api upload image ด้วย Django Rest Framework

## แบบง่ายๆ

### models.py
สร้าง model สำหรับเก็บ path รูปที่จะอัพโหลด

```python
from django.db import models


class SimpleUploadedImage(models.Model):
    # stores the filename of an uploaded image
    image = models.ImageField("Uploaded image")
    timestamp = models.DateTimeField(auto_now_add=True)
```

กำหนดตำแหน่งที่จะให้สร้างไฟล์ โดยแก้ที่ settings.py (เอาไว้ด้านล่าง)

```
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

สร้าง serializers

```python
from rest_framework import serializers
from upload_image.models import SimpleUploadedImage


class SimpleUploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleUploadedImage
        fields = ('pk', 'image', 'timestamp')
```

สร้าง views

```python
from rest_framework import viewsets
from upload_image.api.serializers import SimpleUploadedImageSerializer
from upload_image.models import SimpleUploadedImage


class UploadedImagesViewSet(viewsets.ModelViewSet):
    queryset = SimpleUploadedImage.objects.all()
    serializer_class = SimpleUploadedImageSerializer
```

สร้าง urls

```python
from django.urls import path, include
from rest_framework import routers
from upload_image.api.views import UploadedImagesViewSet

router = routers.DefaultRouter()
router.register('images_simple', UploadedImagesViewSet, 'images_simple')

urlpatterns = [
    path('', include(router.urls)),
]
```

เพิ่ม path ใน helloworld_project/urls.py

```
path('api/', include('upload_image.api.urls'))
```

ถ้าลองรันดูจะสามารถ upload ได้แล้ว แต่ไม่สามารถดูรูปได้ เนื่องจาก django ไม่รองรับ static file ใน /media ต้องแก้ดังนี้

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('upload_image.api.urls'))
]

# เพิ่มตรงนี้ ใช้เฉพาะตอน dev
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```