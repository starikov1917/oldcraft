from product.models import Section
from django.shortcuts import reverse
from oldcraftworkshop.settings import MENU
from product.logic import get_sections


class MenuMixin():
    def get_menu(self):
        return MENU

    def get_available_sections(self):
        return get_sections()

    def __init__(self):
        available_sections = get_sections()