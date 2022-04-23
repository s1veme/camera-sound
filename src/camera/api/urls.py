from rest_framework import routers

from camera.api.views import CameraModelViewSet


router = routers.DefaultRouter()
router.register('cameras', CameraModelViewSet)

urlpatterns = []

urlpatterns += router.urls
