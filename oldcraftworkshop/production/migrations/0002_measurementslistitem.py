# Generated by Django 4.2 on 2023-04-12 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measure', '0001_initial'),
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='measurementsListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure_value', models.CharField(max_length=100, verbose_name='Значение мерки')),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='measure.measure', verbose_name='Мерка')),
                ('production_order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='production.productionorder', verbose_name='Заказ на производство')),
            ],
        ),
    ]
