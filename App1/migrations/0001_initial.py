# Generated by Django 5.0 on 2023-12-23 19:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('cust_name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('sku', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.PositiveBigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('1', 'New'), ('2', 'Packed'), ('2', 'Delivered')], default=1, max_length=100)),
                ('amount', models.PositiveBigIntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.customer')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('1', 'New'), ('2', 'pending'), ('3', 'success'), ('4', 'failed')], default=1, max_length=250)),
                ('amount', models.TextField(blank=True, null=True)),
                ('payment_type', models.TextField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.orders')),
            ],
            options={
                'db_table': 'payments',
            },
        ),
        migrations.CreateModel(
            name='Orderitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('unit_price', models.FloatField(blank=True, null=True)),
                ('qantity', models.PositiveIntegerField(blank=True, null=True)),
                ('total_price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='App1.orders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_item', to='App1.product')),
            ],
            options={
                'db_table': 'orderitems',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('qantity', models.IntegerField()),
                ('product_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App1.product')),
            ],
            options={
                'db_table': 'purchase',
            },
        ),
    ]
