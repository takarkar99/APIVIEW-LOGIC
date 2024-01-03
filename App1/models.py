# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)  # This field type is a guess.
    cust_name = models.CharField(max_length=250, blank=True, null=True)  # This field type is a guess.
    email = models.EmailField(blank=True, null=True)  # This field type is a guess.
    phone = models.CharField(max_length=250)  # This field type is a guess.


    class Meta:
        # managed = False
        db_table = 'customer'


class Product(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)  # This field type is a guess.
    sku = models.CharField(max_length=250,blank=True, null=True)  # This field type is a guess.
    name = models.CharField(max_length=250,blank=True, null=True)  # This field type is a guess.
    price = models.PositiveBigIntegerField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        # managed = False
        db_table = 'product'


STATUS_CHOICE = (
        ('1','New'),
        ('2','Packed'),
        ('2','Delivered'),
        )


class Orders(models.Model):

    id = models.CharField(max_length=250,primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)  # This field type is a guess.
    status = models.CharField(max_length=100, choices=STATUS_CHOICE, default=1)  # This field type is a guess.
    amount = models.PositiveBigIntegerField()  # This field type is a guess.

    class Meta:
        # managed = False
        db_table = 'orders'

class Orderitems(models.Model):

    created_date = models.DateTimeField(auto_now_add=True)  # This field type is a guess.
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='order_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_item')
    unit_price = models.FloatField(blank=True, null=True)  # This field type is a guess.
    qantity = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveBigIntegerField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        # managed = False
        db_table = 'orderitems'


class Purchase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)  # This field type is a guess.
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    qantity = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'purchase'


PAYMENT_STATUS = (
        ('1','New'),
        ('2','pending'),
        ('3','success'),
        ('4','failed')
        )


class Payments(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)  # This field type is a guess.
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    status = models.CharField(max_length=250, choices=PAYMENT_STATUS, default=1)  # This field type is a guess.
    amount = models.TextField(blank=True, null=True)  # This field type is a guess.
    payment_type = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        # managed = False
        db_table = 'payments'