from django.db import models


# Create your models here.
class ShippingType(models.Model):
    name = models.CharField('배송타입', max_length=100, null=False)
    fee = models.IntegerField('배송비', null=True, default=0)
    status = models.BooleanField('사용여부', default=False, null=True)
    create_at = models.DateTimeField('Create Date', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Update Date', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'shipping_type'
        verbose_name_plural = 'shipping_types'
        db_table = 'rt_shipping_type'
        ordering = ('-updated',)

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    name = models.CharField('결제방식', max_length=100, null=False)
    create_at = models.DateTimeField('Create Date', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Update Date', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'payment_type'
        verbose_name_plural = 'payment_types'
        db_table = 'rt_payment_type'
        ordering = ('-updated',)

    def __str__(self):
        return self.name


class CurrencyType(models.Model):
    code = models.CharField('통화코드', max_length=20, null=False)
    name = models.CharField('통화', max_length=50, null=False)
    unit = models.CharField('단위', max_length=10, null=False)
    status = models.BooleanField('사용여부', default=False, null=True)
    create_at = models.DateTimeField('Create Date', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Update Date', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'currency_type'
        verbose_name_plural = 'currency_types'
        db_table = 'rt_currency_type'
        ordering = ('-updated',)

    def __str__(self):
        return self.name
