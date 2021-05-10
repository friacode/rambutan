from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField('연락처', max_length=150, null=True)
    status = models.BooleanField('Status', default=True)
    create_at = models.DateTimeField('Create Date', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Update Date', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'
        db_table = 'rt_customer'
        ordering = ('-updated',)

