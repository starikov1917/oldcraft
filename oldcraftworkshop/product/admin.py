from django.contrib import admin

from .models import Product, ProductImage, RequiredMeasurementSet, SubSection, Section
from django.utils.safestring import mark_safe
# Register your models here.


class ProductPhotoOptionInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    fields = ("image", "title")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'availableQuantity' )

    fields = ('slug' ,'title','rating' ,'isActive' ,'weight' ,'voluametricWeight','productionTime','gpostCode' ,('titlePhoto', 'preview') ,'price' ,'description','isCounatable' ,'availableQuantity','subsection' ,'section')
    inlines = [ProductPhotoOptionInline]
    readonly_fields = ("preview",)
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')



admin.site.register(ProductImage)
admin.site.register(RequiredMeasurementSet)
admin.site.register(Section)
admin.site.register(SubSection)
