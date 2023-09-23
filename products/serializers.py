from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import serializers

from lessons.views import LessonView

from .models import Product, ProductAccess


class ProductSerializer(serializers.ModelSerializer):
    total_lessons_viewed = serializers.SerializerMethodField()
    total_view_time = serializers.SerializerMethodField()
    total_students = serializers.SerializerMethodField()
    purchase_rate = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "name",
            "total_lessons_viewed",
            "total_view_time",
            "total_students",
            "purchase_rate",
        ]

    def get_total_lessons_viewed(self, obj):
        return LessonView.objects.filter(lesson__products=obj, viewed=True).count()

    def get_total_view_time(self, obj):
        return LessonView.objects.filter(lesson__products=obj).aggregate(Sum("view_time"))["view_time__sum"]

    def get_total_students(self, obj):
        return ProductAccess.objects.filter(product=obj).count()

    def get_purchase_rate(self, obj):
        total_users = User.objects.count()
        product_users = ProductAccess.objects.filter(product=obj).count()
        return (product_users / total_users) * 100
