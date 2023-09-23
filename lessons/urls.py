from django.urls import path

from .views import UserLessonListView

urlpatterns = [
    path("lessons/", UserLessonListView.as_view(), name="user-lessons"),
]
