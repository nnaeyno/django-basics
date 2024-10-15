from django.db.models import Avg, Sum, F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

from store.models import Category, Product


def list_products(request):
    products = Product.objects.all()
    data = []
    for product in products:
        product_categories = []
        for category in product.categories.all():
            # parent_category_title, parent_category_id = category.get_direct_category()
            product_categories.append({
                "category_title": category.title,
                "category_id": category.category_id,
                # "parent_category_title": parent_category_title,
                # "parent_category_id": parent_category_id,
            })
        data.append({
            "product_id": product.product_id,
            "name": product.name,
            "description": product.description,
            "price": str(product.price),
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
        # ესე მეწერა თავიდან მარა ჩატში რომ ვიკითხე ლექტორმა პირდაპირი მშობელიო
        # parent_title, parent_id = category.get_main_category()
        parent_title, parent_id = category.get_direct_category()
        data.append({
            "id": category.category_id,
            "title": category.title,
            "parent_title": parent_title,
            "parent_id": parent_id,
        })

    return JsonResponse(data, safe=False)


def list_top_level_categories(request):
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'categories.html', {'categories': categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category, category_id=category_id)
    products = Product.objects.filter(categories=category)
    return render(request, 'category.html', {'category': category, 'products': products})


def get_all_subcategories(category):
    subcategories = category.subcategories.all()
    all_subcategories = list(subcategories)
    for subcategory in subcategories:
        all_subcategories += get_all_subcategories(subcategory)
    return all_subcategories


def category_products(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    subcategories = get_all_subcategories(category)
    products = Product.objects.filter(categories__in=[category] + subcategories).distinct()
    most_expensive = products.order_by('-price').first()
    cheapest = products.order_by('price').first()
    average_price = products.aggregate(average_price=Avg('price'))['average_price']
    overall_worth = products.aggregate(total_worth=Sum(F('price') * F('quantity')))['total_worth']
    context = {
        'category': category,
        'products': products,
        'most_expensive': most_expensive,
        'cheapest': cheapest,
        'average_price': average_price,
        'overall_worth': overall_worth,
    }

    return render(request, 'category_products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)

    context = {
        'product': product
    }

    return render(request, 'product_detail.html', context)