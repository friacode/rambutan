# Generated by Django 3.1.5 on 2021-04-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='수령인'),
        ),
        migrations.AlterField(
            model_name='address',
            name='addr',
            field=models.CharField(max_length=250, verbose_name='주소'),
        ),
        migrations.AlterField(
            model_name='address',
            name='addr_detail',
            field=models.CharField(blank=True, max_length=250, verbose_name='상세주소'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postcode',
            field=models.CharField(max_length=10, verbose_name='우편번호'),
        ),
        migrations.AlterField(
            model_name='address',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='배송지명'),
        ),
    ]
