# Generated by Django 4.2 on 2023-04-12 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_orderitem_quantity_alter_orderitem_order_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyValue', models.CharField(max_length=200, verbose_name='Значение свойства заказ')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.order')),
                ('orderPropertyType', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.orderpropertytype', verbose_name='Тип свойства заказа')),
            ],
        ),
    ]
