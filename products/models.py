from django.contrib.auth.models import User
from django.db import models


# Сущность продукта
class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


# Сущность для сохранения доступов к продукту для пользователя
class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    access_granted = models.DateTimeField(auto_now_add=True)
