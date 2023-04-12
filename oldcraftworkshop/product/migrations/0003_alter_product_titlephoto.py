# Generated by Django 4.2 on 2023-04-12 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
        ('product', '0002_alter_producttype_slug_alter_producttype_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='titlePhoto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gallery.image', verbose_name='Фото анонса'),
        ),
    ]