from django.contrib import admin

from .models import Location, Address,BillingAddress

admin.site.register(Location)
admin.site.register(Address)
admin.site.register(BillingAddress)

# Register your models here.
