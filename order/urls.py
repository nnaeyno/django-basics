from django.urls import path
from . import views

urlpatterns = [
    path("status/", views.get_order_status),
    path("payment/", views.pay_order),
]
