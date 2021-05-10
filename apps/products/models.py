#-*- encoding: utf-8 -*-
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from apps.category.models import Category
from apps.brand.models import Brand


# Create your models here.
class Product(models.Model):
    TYPES = (('CP', '소모품'), ('SP', '서비스 상품'), ('IP', '재고관리 상품'),)
    OPTION = (('NR', '할인 없음'), ('FA', '고정 금액 할인'), ('DR', '할인율'),)

    name = models.CharField('상품이름', max_length=250, null=False)
    code = models.CharField('상품코드', unique=True, max_length=100, null=False)
    summary = models.CharField('상품 간략설명', max_length=250, null=False, default='')
    description = models.TextField('상품 상세설명 ', null=False, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False, default=0)
    types = models.CharField('상품타입', max_length=10, choices=TYPES, null=False)
    orders = models.IntegerField('순서', null=False, default=0)
    price = models.IntegerField('상품가격', null=False, default=0)
    saleOption = models.CharField('할인옵션', max_length=10, choices=OPTION, null=False, default='NR')
    salePrice = models.IntegerField('할인 가격', null=False, default=0)
    sale_ok = models.BooleanField('상품 판매여부', null=False, default=True)
    inventory = models.IntegerField('상품 수량', null=False, default=1)
    create_at = models.DateTimeField('생성일자', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('수정일자', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        db_table = 'rt_product'
        ordering = ('-orders', 'updated')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='administrator/', null=False, default='')
    # thumbnail = models.ImageField(upload_to='administrator/thumbnail', null=False, default='')
    admin_list_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(376, 251)], format='JPEG')
    shop_list_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(253, 300)], format='JPEG')
    create_at = models.DateTimeField('Create Date', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Update Date', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'product_image'
        verbose_name_plural = 'product_images'
        db_table = 'rt_product_image'
        ordering = ('-updated',)


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=150)
    values = models.CharField('Values', max_length=500)
    create_at = models.DateTimeField('Create Date', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Update Date', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'product_option'
        verbose_name_plural = 'product_options'
        db_table = 'rt_product_option'
        ordering = ('-updated',)


class ProductOptionDetail(models.Model):
    OPTION = (('NR', '할인 없음'), ('FA', '고정 금액 할인'), ('DR', '할인율'),)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    code = models.CharField('Code', max_length=100)
    price = models.IntegerField('Price', default=0, null=False)
    saleOption = models.CharField('Sale Option', max_length=10, choices=OPTION, null=False)
    salePrice = models.IntegerField('Sale Price', default=0, null=False)
    quantity = models.IntegerField('Quantity', default=1, null=False)
    sale_ok = models.BooleanField('Sale OK', default=False, null=False)
    create_at = models.DateTimeField('Create Date', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Update Date', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'product_option_detail'
        verbose_name_plural = 'product_option_details'
        db_table = 'rt_product_option_detail'
        ordering = ('-updated',)

    def __str__(self):
        return self.code

