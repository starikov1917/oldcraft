# Generated by Django 4.2 on 2023-05-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0005_alter_billingaddress_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='isUS',
            field=models.BooleanField(default=False, verbose_name='В США'),
        ),
    ]
