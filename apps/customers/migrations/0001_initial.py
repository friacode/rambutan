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
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=150, null=True, verbose_name='연락처')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
                'db_table': 'rt_customer',
                'ordering': ('-updated',),
            },
        ),
    ]
