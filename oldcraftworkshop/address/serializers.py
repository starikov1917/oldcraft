from rest_framework import serializers
from .models import Location, Address, BillingAddress




class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location

        fields = ("pk", "title", "gpostCode", "postcodeFormat", "phoneLength", "countryPhoneCode", "isEU", "isUS", "synonims" )

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("postCode", "city", "addressLine", "firstName", "lastName")

class BillingAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = ("postCode", "city", "addressLine", "firstName", "lastName", "location")