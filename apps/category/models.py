#-*- encoding: utf-8 -*-
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField('카테고리', max_length=100, null=False)
    orders = models.IntegerField('Order', default=0)
    create_at = models.DateTimeField('Create Date', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Update Date', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'administrator'
        verbose_name_plural = 'categories'
        db_table = 'rt_category'
        ordering = ('-orders',)

    def __str__(self):
        return self.name
