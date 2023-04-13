from django.contrib import admin

from .models import Location, Address,BillingAddress

class AddressAdmin(admin.ModelAdmin):
    fields = ("firstName", "lastName", "location", "city", "addressLine", "postCode")
    readonly_fields = ("location",)

admin.site.register(Location)
admin.site.register(Address, AddressAdmin)
admin.site.register(BillingAddress)

# Register your models here.
