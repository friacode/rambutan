from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from apps.address.models import Address
from apps.products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    code = models.CharField('Order Code', unique=True, max_length=100, null=False)
    address = models.OneToOneField(Address, null=True, on_delete=models.CASCADE)
    status = models.CharField('Status', max_length=100, null=False, default='')
    create_at = models.DateTimeField('Create Date', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Update Date', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        db_table = 'rt_order'
        ordering = ('-updated',)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantity', null=True, default=1)
    request_text = models.CharField('Request', max_length=500, null=True)
    price = models.IntegerField('Price', null=True, default=0)
    sale_price = models.IntegerField('Sale Price', null=True, default=0)
    shipping_fee = models.IntegerField('Shipping Fee', null=True, default=0)
    total_price = models.IntegerField('Total Price', null=True, default=0)
    create_at = models.DateTimeField('Create Date', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Update Date', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'order_detail'
        verbose_name_plural = 'order_details'
        db_table = 'rt_order_detail'
        ordering = ('-updated',)
