# Generated by Django 4.2 on 2023-04-13 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
    ]
