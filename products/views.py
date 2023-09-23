from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from lessons.serializers import LessonViewSerializer
from lessons.views import LessonView

from .models import Product, ProductAccess
from .serializers import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Выведение списка уроков по конкретному продукту к которому пользователь имеет доступ
class UserProductLessonListView(generics.ListAPIView):
    serializer_class = LessonViewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        product_id = self.kwargs["product_id"]
        product = get_object_or_404(Product, id=product_id)
        if not ProductAccess.objects.filter(user=self.request.user, product=product).exists():
            raise PermissionDenied("You do not have access to this product")
        return LessonView.objects.filter(user=self.request.user, lesson__products=product)


class ProductStatsView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class ProductUpdateView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
