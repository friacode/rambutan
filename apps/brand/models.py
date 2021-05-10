from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField('상품 브랜드', max_length=100, null=False)
    create_at = models.DateTimeField('Create Date', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Update Date', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
        db_table = 'rt_brand'
        ordering = ('-updated',)

    def __str__(self):
        return self.name
