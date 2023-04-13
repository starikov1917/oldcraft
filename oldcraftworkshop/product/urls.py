
from django.urls import path
from product.views import ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="catalog"),
    path("<slug:section_slug>/", ProductListView.as_view(), name="section"),
    path("<slug:section_slug>/<slug:subsection_slug>/", ProductListView.as_view(), name="subsection"),

]