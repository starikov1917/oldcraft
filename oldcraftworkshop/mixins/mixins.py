from product.models import Section
from django.shortcuts import reverse
from oldcraftworkshop.settings import MENU



class MenuMixin():
    def get_menu(self):
        return MENU


    def get_available_sections(self):
        return Section.objects.all()