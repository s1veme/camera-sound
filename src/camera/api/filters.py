from django_filters import rest_framework as filters

from camera.models import JobReport


class JobReportFilter(filters.FilterSet):

    class Meta:
        model = JobReport
        fields = ['camera', 'created_at']
