from django.contrib import admin
from .models import *

from django.utils.safestring import mark_safe
# Register your models here.


class measureOptionInline(admin.TabularInline):
    model = MeasureOption
    extra = 0
    fields = ("value","rating")
    ordering = ['rating']





@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'rating' )
    fields = ('title', 'type', 'rating', "preview", "image")
    readonly_fields = ("preview",)
    ordering = ["rating"]
    inlines = [measureOptionInline]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')




admin.site.register(MeasureOption)
admin.site.register(MeasureSetItem)
admin.site.register(MeasureType)

# class RowInlineTwo(admin.StackedInline):
#     model = ImgPropertyMaterialProduct
#     filter_horizontal = ('colors',)
#
#
#
# @admin.register(MeasureSet)
# class MeasureSetAdmin(admin.ModelAdmin):
#     model =
#     filter_horizontal = ['MeasureSetItem']