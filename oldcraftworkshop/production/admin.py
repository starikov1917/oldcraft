from django.contrib import admin
from .models import ProductionOrder, ProductionOrderItem,measurementsListItem
# Register your models here.

admin.site.register(ProductionOrder)
admin.site.register(ProductionOrderItem)
admin.site.register(measurementsListItem)