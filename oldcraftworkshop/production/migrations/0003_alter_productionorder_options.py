# Generated by Django 4.2 on 2023-04-13 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_measurementslistitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productionorder',
            options={'verbose_name': 'Заказ на производство', 'verbose_name_plural': 'Заказы на производство'},
        ),
    ]