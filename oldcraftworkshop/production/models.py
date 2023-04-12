from django.db import models

from order.models import Order
from product.models import Product
from measure.models import Measure

# Create your models here.
class ProductionOrder(models.Model):
    production_order_comment = models.TextField(max_length=300, verbose_name="Комментарий к заказу на производство")
    title = models.CharField(max_length=50, verbose_name="Заказчик")
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name="Заказ")

    def __str__(self):
        return self.order.__str__() + " -> " + self.title


class ProductionOrderItem(models.Model):
    production_order = models.ForeignKey(ProductionOrder, on_delete=models.PROTECT, verbose_name="Заказ на производство")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Товар")

    def __str__(self):
        return self.production_order.__str__() + " -> " + self.product.__str__()

class measurementsListItem(models.Model):
    measure_value = models.CharField(max_length=100, verbose_name="Значение мерки")
    production_order = models.ForeignKey(ProductionOrder, on_delete=models.PROTECT, verbose_name="Заказ на производство")
    measure = models.ForeignKey(Measure, on_delete=models.PROTECT, verbose_name="Мерка")

    def __str__(self):
        return self.measure.__str__() + " -> " + self.measure_value