from django.http import HttpResponse
from django.shortcuts import render

def get_order_status(request):
    return HttpResponse("Order status")


def pay_order(request):
    return HttpResponse("Order paid")
