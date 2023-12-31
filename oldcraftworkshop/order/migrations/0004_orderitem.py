# Generated by Django 4.2 on 2023-04-12 10:22

from django.db import migrations, models
import django.db.models.deletion
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_producttype_slug_alter_producttype_title_and_more'),
        ('order', '0003_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderItemPrice', models.DecimalField(decimal_places=2, default=order.models.get_product_price, max_digits=10, verbose_name='Цена в заказе')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.order', verbose_name='заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product', verbose_name='Товар')),
            ],
        ),
    ]
