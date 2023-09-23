from rest_framework import serializers

from .models import Lesson, LessonView


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["title", "video_url", "duration"]


class LessonViewSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    last_viewed = serializers.DateTimeField(source="updated_at")

    class Meta:
        model = LessonView
        fields = ["lesson", "view_time", "viewed", "last_viewed"]
