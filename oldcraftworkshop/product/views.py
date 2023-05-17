from django.shortcuts import render, reverse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Section, SubSection, ProductImage,Product, Product_option
# Create your views here.
from mixins.mixins import MenuMixin
from .logic import get_subsection, get_sections, get_section, get_subsections, get_products, get_product
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import  ModelViewSet
import json
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from material.models import RequiredMaterialType, Material,MaterialType

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
        available_sections = get_sections()

        if "subsection_slug" in self.kwargs:
            neigbors = get_subsections(self.kwargs['section_slug'])
            pushed_subsection_slug = self.kwargs['subsection_slug']
            l =  list(neigbors)
            temp_subsection = list(filter(lambda subsection: subsection.slug == pushed_subsection_slug, l)).pop()

            context["title"] = temp_subsection.title
            catalog_navigation = [{
                "title": "Back",
                "url": reverse("section", kwargs={"section_slug": self.kwargs['section_slug']}),
                "is_pushed": False}
            ]
            catalog_navigation +=  list(map(lambda subsection: {"title":subsection.title,
                                                                    "url":subsection.get_absolute_url(),
                                                                    "is_pushed": pushed_subsection_slug == subsection.slug},
                                                neigbors))
        elif "section_slug" in self.kwargs:
            neigbors = get_subsections(self.kwargs['section_slug'])
            l = list(neigbors)
            temp_section = list(filter(lambda s: s.slug == self.kwargs['section_slug'], list(available_sections))).pop()
            context["title"] = temp_section.title
            catalog_navigation = [{
                "title": "All products",
                "url": reverse("catalog"),
                "is_pushed": False}
            ]
            catalog_navigation += list(map(lambda section: {"title": section.title,
                                                               "url": section.get_absolute_url(),
                                                               "is_pushed": False},
                                           neigbors))
        else:
            catalog_navigation = [{"title":"All products",
                                       "url": "",
                                       "is_pushed": True}]
            neigbors = list(available_sections)
            catalog_navigation += list(map(lambda section: {"title": section.title,
                                                               "url": section.get_absolute_url(),
                                                               "is_pushed": False},
                                           neigbors))
        context["sections"] = available_sections
        context["catalog_navigation"] = catalog_navigation
        context["menu"] = self.get_menu()

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
        return Product.objects.all()


    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['title'] = product.title
        context["menu"] = self.get_menu()
        context["sections"] = self.get_available_sections()
        context['gallery'] = [product.titlePhoto.image] # фото анонса
        context['gallery'] += list(map(lambda product: product.image, list(ProductImage.objects.filter(product__slug=product.slug))))  # все связанные фото
        if product.has_options:
            context["options"] = Product_option.objects.filter(product=product, isActive=True)

        requiredMaterialType = RequiredMaterialType.objects.filter(product=product)
        if requiredMaterialType:
            req_type = requiredMaterialType.first()
            context["materials"] = Material.objects.filter(
                is_active=True,
                materialType=req_type.materialType,
                availableQuantity__gte=req_type.requiredQuantity)
        return context




class ProductAPIViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"

class GetCartWeight(APIView):

    def post(self, request):
        print("----------", request.data)
        if "cart" in request.data and request.data["cart"]:
            print("----------", request.data["cart"])
            cart = json.loads(request.data["cart"])
            slugs = list(cart.keys())
            products = Product.objects.filter(slug__in=slugs).values("pk", "slug", "weight", "price")
            subtotal = 0
            total_weight = 0
            for product in list(products):
                quantity = int(cart[product["slug"]]["quantity"])
                subtotal += quantity * float(product["price"])
                total_weight += quantity * product["weight"]

            if total_weight > 0:
                return Response({"weight":total_weight, "subtotal":subtotal})
            else:
                resp = Response({"error": "cart is empty"})
                resp.status_code = 400
                return resp

        else:
            resp = Response({"error":"cart isn't found"})
            resp.status_code = 400

            return  resp

        # return Response({"weight": 156})