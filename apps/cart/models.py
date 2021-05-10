from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # option = models.ForeignKey(ProductOptionDetail, on_delete=models.CASCADE)
    status = models.BooleanField('Status', default=True)
    quantity = models.IntegerField('Quantity', default=1)
    create_at = models.DateTimeField('Create Date', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Update Date', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'
        db_table = 'rt_cart'
        ordering = ('-updated',)
