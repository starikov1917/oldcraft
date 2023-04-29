"""oldcraftworkshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from measure.views import MeasuresList
from django.conf.urls.static import static
from django.conf import settings
from product.views import SectionListViews, ProductAPIViewSet, GetCartWeight
from .static_pages import static_page
from basket.basket import basket
from rest_framework import routers
from gallery.views import titleImageApiView
from order.views import create_order
from address.views import BookListView
from shipping.views import ShippingCost




urlpatterns = [

    path('', SectionListViews.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path("measures/", MeasuresList.as_view()),
    path("api/v1/product/", ProductAPIViewSet.as_view({'get': 'list'})),
    path("api/v1/product/<slug:slug>/", ProductAPIViewSet.as_view({"put": "update", "get":'retrieve',"delete":"destroy"})),
    path("api/v1/image/<int:pk>/", titleImageApiView.as_view(), name="image-retrieve"),
    path("api/v1/location/", BookListView.as_view(), name="location-list"),
    path("api/v1/cartWeight/", GetCartWeight.as_view()),
    path("api/v1/shippingCost/", ShippingCost.as_view()),
    path("catalog/", include('product.urls')),
    path("basket/", static_page("Cart", "basket/basket.html"), name="basket"),
    path("checkout/", create_order, name="checkout"),

    path('__debug__/', include('debug_toolbar.urls')),


]



## Статические страницы
urlpatterns += [
    path("about/", static_page("About", "static_pages/about.html"), name="about"),
    path("payment/", static_page("Payments", "static_pages/payment.html"), name="payment"),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)












