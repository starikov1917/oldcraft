from django.shortcuts import render
from mixins.mixins import MenuMixin
from product.logic import get_sections


def static_page(title: str="OldCraft workshop", tamplate="base.html"):

    def page(request):
        mexin = MenuMixin()
        return render(request, tamplate,
                      context={"title": title,
                               "menu": mexin.get_menu(),
                               "sections": get_sections()})

    return page