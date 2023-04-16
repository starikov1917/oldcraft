from django.shortcuts import render
from mixins.mixins import MenuMixin
from product.logic import get_sections


def about(request):
    mexin = MenuMixin()
    return render(request, "static_pages/about.html",
                  context={"title":"About",
                           "menu" : mexin.get_menu(),
                           "sections" : get_sections()})

def payment(request):
    mexin = MenuMixin()
    return render(request, "static_pages/about.html",
                  context={"title":"Payment",
                           "menu" : mexin.get_menu(),
                           "sections" : get_sections()})