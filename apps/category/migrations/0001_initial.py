# Generated by Django 3.1.5 on 2021-04-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='카테고리')),
                ('orders', models.IntegerField(default=0, verbose_name='Order')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
            ],
            options={
                'verbose_name': 'administrator',
                'verbose_name_plural': 'categories',
                'db_table': 'rt_category',
                'ordering': ('-orders',),
            },
        ),
    ]
