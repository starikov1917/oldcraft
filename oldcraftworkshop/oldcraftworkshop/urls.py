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
from product.views import ProductListView, SectionListVies
from .static_pages import static_page
from basket.basket import basket

urlpatterns = [
    path('', SectionListVies.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path("measures/", MeasuresList.as_view()),
    path("catalog/", include('product.urls')),
    path("basket/", static_page("Cart", "basket/basket.html"), name="basket")
]

## Статические страницы
urlpatterns += [
    path("about/", static_page("About", "static_pages/about.html"), name="about"),
    path("payment/", static_page("Payments", "static_pages/payment.html"), name="payment"),


]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)