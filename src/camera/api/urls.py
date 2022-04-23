from rest_framework import routers

from camera.api.views import CameraModelViewSet, JobReportModelViewSet


router = routers.DefaultRouter()
router.register('cameras', CameraModelViewSet)
router.register('job-report', JobReportModelViewSet)

urlpatterns = []

urlpatterns += router.urls
