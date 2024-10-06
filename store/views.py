from django.http import HttpResponse
from django.shortcuts import render


def get_products(request):
    return HttpResponse("In stock products")


def sort_products(request):
    return HttpResponse("Sorted products")
