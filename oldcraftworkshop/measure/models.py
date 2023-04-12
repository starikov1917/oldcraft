from django.db import models

# Create your models here.
class MeasureType(models.Model):
    title = models.CharField(max_length=50, verbose_name="Тип мерки")
    slug = models.SlugField(unique=True, max_length=20)

    def __str__(self):
        return self.title

class MeasureSet(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название набора мерок")
    description = models.TextField(max_length=300, blank=True, null=True, verbose_name="Описание набора мерок")

    def __str__(self):
        return self.title

class Measure(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название мерки")
    description = models.CharField(max_length=300, blank=True, null=True, verbose_name="Описание мерки")
    type = models.ForeignKey(MeasureType, on_delete=models.PROTECT, verbose_name="Тип мерки")
    rating = models.IntegerField(default=100, verbose_name="Рейтинг")
    image = models.ImageField(verbose_name="фото мерки",upload_to="images/measures")


    def __str__(self):
        return self.title


class MeasureSetItem(models.Model):
    measure = models.ForeignKey(Measure, on_delete=models.PROTECT, verbose_name="Мерка")
    measureSet = models.ForeignKey(MeasureSet, on_delete=models.PROTECT, verbose_name="Набор мерок")

    def __str__(self):
        return self.measureSet.__str__() + " -> " + self.measure.__str__()

class MeasureOption(models.Model):
    measure = models.ForeignKey(Measure, on_delete=models.PROTECT, verbose_name="Мерка")
    value = models.CharField(max_length=50, verbose_name="Вариант мерки")
    rating = models.IntegerField(verbose_name="Рейтинг")

    def __str__(self):
        return self.measure.__str__() + "->" + str(self.value)

