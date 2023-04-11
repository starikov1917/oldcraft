from django.db import models

# Create your models here.


class ShippingMethod(models.Model):
    title = models.TextField(max_length=100, blank=False, verbose_name="Метод доставки")
    code = models.TextField(max_length=20, blank=False, unique=True, verbose_name="код типа доставки")

    def __str__(self):
        return self.title
