from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Section, SubSection
# Create your views here.

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        if "subsection_slug" in self.kwargs:
            return Product.objects.filter(subsection__slug=self.kwargs["subsection_slug"])
        elif "section_slug" in self.kwargs:
            return Product.objects.filter(section__slug=self.kwargs["section_slug"])
        else:
            return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = 'Catalog'
        catalog_navigation = []
        if "subsection_slug" in self.kwargs:
            neigbors = SubSection.objects.filter(section__slug=self.kwargs['section_slug'])
            subsection = get_object_or_404(SubSection, slug=self.kwargs['subsection_slug'])
            section = subsection.section

            catalog_navigation = [{"title":"Back",
                                   "url":section.get_absolute_url(),
                                   "is_pushed": False}]
            catalog_navigation +=  list(map(lambda subsection: {"title":subsection.title,
                                                                "url":subsection.get_absolute_url(),
                                                                "is_pushed": self.kwargs['subsection_slug'] == subsection.slug},
                                            neigbors))
            context["title"] = subsection.title
        elif "section_slug" in self.kwargs:
            neigbors = SubSection.objects.filter(section__slug=self.kwargs['section_slug'])
            section = get_object_or_404(Section, slug=self.kwargs['section_slug'])
            context["title"] = section.title
            catalog_navigation = [{"title":"Back",
                                   "url":"/catalog/",
                                   "is_pushed": False}]
            catalog_navigation +=  list(map(lambda subsection: {"title":subsection.title,
                                                                "url":subsection.get_absolute_url(),
                                                                "is_pushed": False},
                                            neigbors))
        else:
            neigbors = Section.objects.all()
            catalog_navigation += list(map(lambda section: {"title": section.title,
                                                               "url": section.get_absolute_url(),
                                                               "is_pushed": False},
                                           neigbors))

        context["catalog_navigation"] = catalog_navigation
        return context