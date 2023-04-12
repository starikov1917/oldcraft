# Generated by Django 4.2 on 2023-04-12 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0004_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Группа материалов')),
                ('slug', models.SlugField(unique=True, verbose_name='Код группы материалов')),
            ],
        ),
        migrations.CreateModel(
            name='requiredMaterialType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requiredQuantity', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Необходимое количество')),
                ('materialType', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='material.materialtype')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Материал')),
                ('slug', models.SlugField(max_length=20, verbose_name='Код материала')),
                ('availableQuantity', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Доступное количество')),
                ('image', models.ImageField(upload_to='images/materials')),
                ('materialType', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='material.materialtype')),
            ],
        ),
    ]
