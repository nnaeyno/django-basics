from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.list_products),
    path("product/", views.get_product),
    path("categories/", views.get_categories),
    path("category/", views.list_top_level_categories),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
]
