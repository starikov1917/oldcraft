from django.contrib import admin
from .models import OrderStatus, Order, OrderItem, OrderProperty, OrderPropertyType
# Register your models here.

admin.site.register(OrderStatus)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderProperty)
admin.site.register(OrderPropertyType)