from django.urls import path
from .views import CustomerAPI, OrderAPI, ProductAPI, PaymnetAPI


urlpatterns = [
    path('customer/', CustomerAPI, name='customer_urls'),
    path('order/', OrderAPI.as_view(), name='order_urls'),
    path('product/', ProductAPI.as_view(), name='product_urls'),
    path('payment/', PaymnetAPI.as_view(), name='payment_urls')
    # path('orderitem/', OrderItemAPI.as_view(), name='Orderitem_urls'),
]