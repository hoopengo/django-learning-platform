from django.urls import path

from .views import (
    ProductCreateView,
    ProductListCreateView,
    ProductStatsView,
    ProductUpdateView,
    UserProductLessonListView,
)

urlpatterns = [
    path("products/", ProductListCreateView.as_view(), name="product-list-create"),
    path("products/<int:product_id>/lessons/", UserProductLessonListView.as_view(), name="user-product-lessons"),
    path("products/stats/", ProductStatsView.as_view(), name="product-stats"),
    path("products/create/", ProductCreateView.as_view(), name="product-create"),
    path("products/update/<int:pk>/", ProductUpdateView.as_view(), name="product-update"),
]
