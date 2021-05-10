from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('배송지명', max_length=100, blank=True)
    name = models.CharField('수령인', max_length=100, blank=True)
    addr = models.CharField('주소', max_length=250)
    addr_detail = models.CharField('상세주소', max_length=250, blank=True)
    postcode = models.CharField('우편번호', max_length=10)
    baseDelivery = models.BooleanField('기본배송지', default=False)
    create_at = models.DateTimeField('Create Date', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Update Date', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'
        db_table = 'rt_address'
        ordering = ('-id',)
