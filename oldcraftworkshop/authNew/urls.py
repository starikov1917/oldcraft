from django.urls import path, include
from .views import GetAccess, ConfirmEmail, Logout


urlpatterns = [
    path("getaccess/", GetAccess.as_view()),
    path("confirmemail/", ConfirmEmail.as_view()),
    path("logout/", Logout.as_view(), name="logout")
]
