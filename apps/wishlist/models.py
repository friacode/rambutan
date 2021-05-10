from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from apps.products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    create_at = models.DateTimeField('Create Date', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Update Date', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'
        db_table = 'rt_wishlist'
        ordering = ('-updated',)

