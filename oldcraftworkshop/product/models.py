from django.db import models
from django.shortcuts import reverse
from gallery.models import Image
from measure.models import MeasureSet
# Create your models here.
class ProductType(models.Model):
    title = models.CharField(max_length=50, verbose_name="Тип товара")
    slug = models.SlugField(unique=True, verbose_name="Символьный код")

    class Meta:
        verbose_name = "Тип товаров"
        verbose_name_plural = "Типы товаров"

def get_defoult():
    return ProductType.objects.get(id=1)


class Section(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/sectoins")
    slug = models.SlugField(max_length=50, unique=True, verbose_name="Slug")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Раздел товаров"
        verbose_name_plural = "Разделы товаров"

    def get_absolute_url(self):
        return reverse("section", kwargs={'section_slug':self.slug})



class SubSection(models.Model):
    title = models.CharField(max_length=200)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=50, unique=True, verbose_name="Slug")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Подраздел товаров"
        verbose_name_plural = "Подразделы товаров"

    def get_absolute_url(self):
        return reverse("subsection", kwargs={'section_slug':self.section.slug, "subsection_slug":self.slug})

class Product(models.Model):

    slug = models.SlugField(max_length=50, unique=True, verbose_name="Slug")
    title = models.CharField(max_length=150, verbose_name="название")
    rating = models.IntegerField(default=100, verbose_name="Рейтинг")
    isActive = models.BooleanField(default=True, verbose_name="Активный?")
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updatedAt = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    weight = models.IntegerField(default=1000, verbose_name="Вес")
    voluametricWeight = models.IntegerField(default=1000, verbose_name="Объемный вес")
    productionTime = models.TimeField(blank=True, verbose_name="Время на производство")
    gpostCode = models.IntegerField(default=1, verbose_name="Код товара почты грузии")
    titlePhoto = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Фото анонса")
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Базовая цена")
    description = models.TextField(max_length=1000, blank=True, verbose_name="Подробное описание")
    isCounatable = models.BooleanField(default=True)
    availableQuantity = models.IntegerField(default=0, verbose_name="Доступное количество")
    subsection = models.ForeignKey(SubSection, null=True, blank=True, on_delete=models.PROTECT)
    section = models.ForeignKey(Section, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Товар")
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title

class RequiredMeasurementSet(models.Model):
    measureSet = models.ForeignKey(MeasureSet, on_delete=models.PROTECT, verbose_name="Требуемый набор")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Товар")

    def __str__(self):
        return self.product.__str__() + " -> " + self.measureSet.__str__()

