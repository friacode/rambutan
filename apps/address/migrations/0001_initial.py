# Generated by Django 3.1.5 on 2021-04-07 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Title')),
                ('addr', models.CharField(max_length=250, verbose_name='Address')),
                ('addr_detail', models.CharField(blank=True, max_length=250, verbose_name='Address Detail')),
                ('postcode', models.CharField(max_length=10, verbose_name='Post Code')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
                'db_table': 'rt_address',
                'ordering': ('-updated',),
            },
        ),
    ]
