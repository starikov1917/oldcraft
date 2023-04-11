from django.db import models
from shipping.models import ShippingMethod
from address.models import Address, BillingAddress

# Create your models here.

class OrderPropertyType(models.Model):
    title = models.CharField(max_length=100, verbose_name="Свойство заказа")
    code = models.CharField(max_length=20,  unique=True, verbose_name="код код свойства заказ")

    def __str__(self):
        return self.title

class OrderStatus(models.Model):
    slug = models.SlugField(max_length=200, verbose_name="Код статуса")
    title = models.CharField(max_length=50, verbose_name="Статус заказа")
    rating = models.IntegerField(default=100, verbose_name="порядок выдачи")
    color = models.CharField(default="#ffffff", max_length=7, verbose_name="цвет статуса")

    def __str__(self):
        return self.title

def get_first_status():
    return OrderStatus.objects.get(id=1)



class Order(models.Model):
    orderNumber = models.CharField(max_length=10, unique=True, blank=False, null=False, verbose_name="Номер заказа")
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updatedAt = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    orderComment = models.TextField(max_length=500, null=True, blank=True, verbose_name="Комментарий к заказу")
    shippingCost = models.DecimalField(decimal_places=2, max_digits=10,verbose_name="Стоимость доставки")
    shippingMethod = models.ForeignKey(ShippingMethod, on_delete=models.PROTECT,  verbose_name="Способ доставки")
    address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True, verbose_name="Адресс доставки")
    billingAddress = models.ForeignKey(BillingAddress, null=True, on_delete=models.PROTECT, verbose_name="Адрес счета")
    orderStatus = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, default=get_first_status)

    def __str__(self):
        return self.orderNumber