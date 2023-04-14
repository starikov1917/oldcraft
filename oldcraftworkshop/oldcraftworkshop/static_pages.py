from django.shortcuts import render
from mixins.mixins import MenuMixin



def about(request):
    mexin = MenuMixin()
    return render(request, "static_pages/about.html",
                  context={"title":"About",
                           "menu" : mexin.get_menu(),
                           "sections" : mexin.get_available_sections()})

def payment(request):
    mexin = MenuMixin()
    return render(request, "static_pages/about.html",
                  context={"title":"Payment",
                           "menu" : mexin.get_menu(),
                           "sections" : mexin.get_available_sections()})