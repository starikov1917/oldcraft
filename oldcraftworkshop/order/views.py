from django.shortcuts import render

# Create your views

def create_order(request):
    return render(request, "order.html", context={
        "title": "Checkout page"
    })