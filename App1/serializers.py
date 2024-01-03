from rest_framework import serializers
from .models import Customer, Orders, Product, Orderitems, Purchase, Payments

class CustomSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orderitems
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'