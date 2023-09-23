from django.contrib.auth.models import User
from django.db import models

from products.models import Product


# Сущность урока
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    duration = models.PositiveIntegerField()  # Длина видео в секундах
    products = models.ManyToManyField(Product)


# Сущность статистики к уроку для пользователя
class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    view_time = models.PositiveIntegerField(default=0)  # Время просмотра в секундах
    viewed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Выставления статуса "viewed"
        # если пользователь просмотрел более 80% ролика.
        if self.view_time >= self.lesson.duration * 0.8:
            self.viewed = True
        super().save(*args, **kwargs)
