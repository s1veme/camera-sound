from django.db import models


class Camera(models.Model):
    title = models.CharField('Название камеры', max_length=1028)

    def __str__(self):
        return self.title


class JobReport(models.Model):
    camera = models.ForeignKey(Camera, verbose_name='Камера', on_delete=models.CASCADE)

    statistics = models.TextField('Статистика', blank=True, null=True)
    video = models.FileField("Видео", upload_to="videos/%Y/%m/%d/")

    created_at = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return str(self.camera)
