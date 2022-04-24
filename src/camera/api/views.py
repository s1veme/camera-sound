from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import JSONParser

from camera.api.serializers import (
    CameraSerializer, CameraCreateSerializer,
    JobReportSerializer
)
from camera.api.parsers import MultipartJsonParser
from camera.api.filters import JobReportFilter

from camera.service import convert_camera_parameters, create_many_test_parameters
from camera.models import Camera, JobReport


class CameraModelViewSet(ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

    serializer_classes = {
        'create': CameraCreateSerializer,
    }

    default_serializer_class = CameraSerializer

    parser_classes = [MultipartJsonParser, JSONParser]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,
                                           self.default_serializer_class)

    @action(methods=['POST'], detail=False, url_path='create-report')
    def create_report(self, request, *args, **kwargs):
        data = request.data.copy()

        if not data['statistics']:
            return Response({'error': 'pass statistics as json'}, status=status.HTTP_400_BAD_REQUEST)

        statistics = convert_camera_parameters(data['statistics'])
        statistics = create_many_test_parameters(statistics, 2)
        data['statistics'] = statistics
        data['video'] = request.FILES['video']

        serializer = JobReportSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class JobReportModelViewSet(ModelViewSet):
    queryset = JobReport.objects.all()
    serializer_class = JobReportSerializer
    
    filterset_class = JobReportFilter

