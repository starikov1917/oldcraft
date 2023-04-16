from django.contrib import admin

from .models import Product, ProductImage, RequiredMeasurementSet, SubSection, Section
# Register your models here.




admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(RequiredMeasurementSet)
admin.site.register(Section)
admin.site.register(SubSection)
