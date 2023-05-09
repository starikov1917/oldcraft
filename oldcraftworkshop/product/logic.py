from .models import Section, SubSection, Product
from django.shortcuts import get_object_or_404

def get_sections():
    return Section.objects.all()

def get_subsections(section_slug: str):
    return SubSection.objects.filter(section__slug=section_slug)

def get_subsection(subsection_slug: str):
    return get_object_or_404(SubSection, slug=subsection_slug)

def get_section(section_slug: str):
    return get_object_or_404(Section, slug=section_slug)


def get_products(**kwargs):
    if "subsection_slug" in kwargs:
        return Product.objects.filter(subsection__slug=kwargs["subsection_slug"], availableQuantity__gt=0).select_related("titlePhoto")
    elif "section_slug" in kwargs:
        return Product.objects.filter(section__slug=kwargs["section_slug"], availableQuantity__gt=0).select_related("titlePhoto")
    else:
        return Product.objects.filter(availableQuantity__gt=0).select_related("titlePhoto")

def get_product(slug: str):
    return get_object_or_404(Product, slug=slug)

