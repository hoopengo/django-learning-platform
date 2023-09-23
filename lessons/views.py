from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import LessonView
from .serializers import LessonViewSerializer


# Выведение списка всех уроков по всем продуктам к которым пользователь имеет доступ
class UserLessonListView(generics.ListAPIView):
    serializer_class = LessonViewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LessonView.objects.filter(user=self.request.user)
