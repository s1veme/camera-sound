from django.contrib import admin

from .models import Camera, JobReport


@admin.register(Camera)
class CameraModelAdmin(admin.ModelAdmin):
    fields = ('title',)

    list_display = ('id', 'title')


@admin.register(JobReport)
class JobReportModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'camera')
