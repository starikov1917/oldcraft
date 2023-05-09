from .views import OrderCreate
from django.urls import path


urlpatterns = [
    path("api/v1/order/", OrderCreate.as_view()),
]