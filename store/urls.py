from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.list_products),
    path("product/", views.get_product),
    path("categories/", views.get_categories),
    path("category/", views.list_top_level_categories),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('category/<int:category_id>/products/', views.category_products, name='category_products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
