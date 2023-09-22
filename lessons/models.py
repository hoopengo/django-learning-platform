from django.db import models
from products.models import Product
from users.models import User


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_seconds = models.PositiveIntegerField()
    products = models.ManyToManyField(Product, related_name="lessons")

    def __str__(self):
        return self.title


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed_time_seconds = models.PositiveIntegerField()
    status = models.BooleanField(default=False)  # Просмотрено или нет

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title} ({'Просмотрено' if self.status else 'Не просмотрено'})"
