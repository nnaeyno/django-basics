from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.list_products),
    path("product/", views.get_product),

    path("categories/", views.get_categories),
]
