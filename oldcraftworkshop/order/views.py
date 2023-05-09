from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from product.models import Product
from address.models import Location, Address, BillingAddress
from address.serializers import AddressSerializers, LocationListSerializer, BillingAddressSerializers
from .models import Order, OrderItem
from shipping.models import ShippingMethod
from shipping.logic import calculate_postage
# Create your views

def create_order(request):
    return render(request, "order.html", context={
        "title": "Checkout page"
    })


class  OrderCreate(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request):
        data = request.data
        cart = json.loads(data["cart"])
        products_in_cart = Product.objects.filter(slug__in=cart)
        print(data)
        order_weight = 0 # посчитать вес корзины
        order_subtotal= 0 # посчитать промежуточный итог

        is_enouth = True

        for item in products_in_cart:
            if item.getQuantity() >= cart[item.getSlug()]["quantity"]:

                item.setQuantity(item.getQuantity() - cart[item.getSlug()]["quantity"])
                order_weight +=  cart[item.getSlug()]["quantity"]  * item.getWeight()
                order_subtotal += cart[item.getSlug()]["quantity"] * item.getPrice()
            else:
                errors.append({"Not enough": item})
                is_enouth = False
        if not is_enouth:
            print("недостаточно товара")
            return Response(status=400)

        location = Location.objects.filter(title=data["shipping-country"])

        if location:
            location = location.first()
        else:
            print("плохая локация")
            return Response(status=400)

        billing_address_serializer = BillingAddressSerializers(data={
            "postCode": data["billing-index"],
            "city": data["billing-city"],
            "addressLine": data["billing-address"],
            "firstName": data["billing-first-name"],
            "lastName":  data["billing-last-name"],
            "location":  data["billing-country"]
        })
        shipping_address_serializer = AddressSerializers(data={
            "postCode": data["shipping-index"],
            "city": data["shipping-city"],
            "addressLine": data["shipping-address"],
            "firstName": data["shipping-first-name"],
            "lastName": data["shipping-last-name"]
        })


        if shipping_address_serializer.is_valid() and billing_address_serializer.is_valid():
            shipping_address_data = shipping_address_serializer.data
            address = Address(**shipping_address_data, location=location)
            billing_address = BillingAddress(**billing_address_serializer.data)
            address.save()
            billing_address.save()
            order = Order(
                orderComment=data["order-comment"],
                shippingCost=calculate_postage(
                    location.pk,
                    order_weight,
                    order_subtotal
                ), ## посчитать стоимость доставки
                shippingMethod=ShippingMethod.objects.all().first(),
                address=address,
                billingAddress=billing_address,
                user=request.user
            )
            print(order)
            order.save()


            if is_enouth:
                for item in products_in_cart:
                    orderItem =  OrderItem(
                        order=order,
                        product=item,
                        quantity=cart[item.getSlug()]["quantity"],
                        orderItemPrice=item.getPrice()
                    )
                    orderItem.save()
                    item.save()


        return Response(status=200)