from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from store.models import Category, Product


def list_products(request):
    products = Product.objects.all()
    data = []
    for product in products:
        product_categories = []
        for category in product.categories.all():
            parent_category_title, parent_category_id = category.get_direct_category()
            product_categories.append({
                "category_title": category.title,
                "parent_category_title": parent_category_title,
                "parent_category_id": parent_category_id,
            })
        data.append({
            "product_id": product.product_id,
            "name": product.name,
            "description": product.description,
            "price": str(product.price),  # Convert Decimal to string for JSON serialization
            "product_image": product.product_image.url if product.product_image else None,
            "categories": product_categories
        })
    return JsonResponse(data, safe=False)


def get_product(request):
    return HttpResponse("One product")


def get_categories(request):
    categories = Category.objects.all()
    data = []
    for category in categories:
        parent_title, parent_id = category.get_main_category()
        data.append({
            "id": category.category_id,
            "title": category.title,
            "parent_title": parent_title,
            "parent_id": parent_id,
        })

    return JsonResponse(data, safe=False)


