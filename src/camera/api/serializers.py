from rest_framework import serializers

from camera.models import Camera, JobReport


class JobReportSerializer(serializers.ModelSerializer):
    camera_title = serializers.CharField(source='camera.title', read_only=True)

    class Meta:
        model = JobReport
        fields = ['id', 'camera', 'camera_title', 'statistics', 'video', 'report_xlsx', 'created_at']


class CameraSerializer(serializers.ModelSerializer):
    job_reports = JobReportSerializer(source='jobreport_set', many=True)

    class Meta:
        model = Camera
        fields = ['id', 'title', 'job_reports']


class CameraCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ['id', 'title']
