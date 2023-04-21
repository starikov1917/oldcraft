from django.shortcuts import render, reverse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Section, SubSection, ProductImage,Product
# Create your views here.
from mixins.mixins import MenuMixin
from .logic import get_subsection, get_sections, get_section, get_subsections, get_products, get_product
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import  ModelViewSet

from .serializers import ProductSerializer
class ProductListView(MenuMixin, ListView):
    model = Product

    def get_queryset(self):
        if "subsection_slug" in self.kwargs:
            return get_products(subsection_slug=self.kwargs["subsection_slug"])
        elif "section_slug" in self.kwargs:
            return get_products(section_slug=self.kwargs["section_slug"])
        else:
            return get_products()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = 'Catalog'
        catalog_navigation = []
        pushed_subsection_slug = str()

        if "subsection_slug" in self.kwargs:

            subsection = get_subsection(self.kwargs['subsection_slug'])
            context["title"] = subsection.title
            pushed_subsection_slug = subsection.slug
            if subsection.section.slug != self.kwargs['section_slug']:
                raise Http404(
                    "Wrong subsection or section slug"
                )


        if "section_slug" in self.kwargs:
            neigbors = get_subsections(self.kwargs['section_slug'])
            section = get_section(self.kwargs['section_slug'])
            context["title"] = section.title
            catalog_navigation = [{"title":"Back",
                                   "url": reverse("catalog"),
                                   "is_pushed": False}]
            catalog_navigation +=  list(map(lambda subsection: {"title":subsection.title,
                                                                "url":subsection.get_absolute_url(),
                                                                "is_pushed": pushed_subsection_slug == subsection.slug},
                                            neigbors))
        else:
            catalog_navigation = [{"title":"All products",
                                   "url": "",
                                   "is_pushed": True}]
            neigbors = Section.objects.all()
            catalog_navigation += list(map(lambda section: {"title": section.title,
                                                               "url": section.get_absolute_url(),
                                                               "is_pushed": False},
                                           neigbors))

        context["catalog_navigation"] = catalog_navigation
        context["menu"] = self.get_menu()
        context["sections"] = self.get_available_sections()
        return context


class SectionListViews(MenuMixin, ListView):
    model = Section

    def get_queryset(self):
        # тут можно отфильтровать по активности раздела
        return Section.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'OldCraft workshop'
        context["menu"] = self.get_menu()
        context["sections"] = self.get_available_sections()
        return context

class ProductDetailView(MenuMixin, DetailView):
    model = Product
    slug_url_kwarg = 'product_slug'

    def get_queryset(self):
        return get_products()

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['title'] = product.title
        context["menu"] = self.get_menu()
        context["sections"] = self.get_available_sections()
        context['gallery'] = [product.titlePhoto.image] # фото анонса
        context['gallery'] += list(map(lambda product: product.image, list(ProductImage.objects.filter(product__slug=product.slug))))  # все связанные фото

        return context




class ProductAPIViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
