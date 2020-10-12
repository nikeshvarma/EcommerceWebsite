# Generated by Django 3.0.8 on 2020-10-12 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('PRODUCTS', '0002_auto_20201012_1731'),
        ('USER', '0002_usercart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='cart_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PRODUCTS.Product'),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
