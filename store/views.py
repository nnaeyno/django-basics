from django.http import HttpResponse
from django.shortcuts import render


def list_products(request):
    return HttpResponse("In stock products")


def get_product(request):
    return HttpResponse("One product")
