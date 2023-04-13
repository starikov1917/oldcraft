from django.contrib import admin
from .models import OrderStatus, Order, OrderItem, OrderProperty, OrderPropertyType
from address.models import Address, BillingAddress
from django.utils.safestring import mark_safe
# Register your models here.



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    fields = ("product","orderItemPrice","quantity")
    can_delete = False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ("createdAt", 'orderNumber', "orderStatus", "shippingCost", "orderComment", 'get_order_items_list')
    list_display_links = ("createdAt", 'orderNumber', "orderStatus")
    search_fields = ("createdAt", 'orderNumber', "orderStatus")
    list_filter = ('orderNumber', "orderStatus")
    fields = ("orderNumber", "createdAt", "updatedAt", 'orderStatus', "orderComment",  'shippingMethod',"shippingCost", 'address', 'billingAddress')
    readonly_fields = ("orderNumber", "createdAt", "updatedAt",)
    inlines = [OrderItemInline]
    def get_order_items_list(self, object: Order):
        return mark_safe("<br>".join(list(map(lambda item: item.product.title + " (" + str(item.quantity) + " шт)", OrderItem.objects.filter(order=object.id)))))

    get_order_items_list.short_description = "состав заказ"




@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass




admin.site.register(OrderStatus)
admin.site.register(OrderProperty)
admin.site.register(OrderPropertyType)