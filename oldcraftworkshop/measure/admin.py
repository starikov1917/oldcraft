from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(MeasureOption)
admin.site.register(MeasureSetItem)
admin.site.register(MeasureType)
admin.site.register(MeasureSet)
admin.site.register(Measure)