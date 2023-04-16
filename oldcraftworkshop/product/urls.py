
from django.urls import path
from product.views import ProductListView, ProductDetailView

urlpatterns = [
    path("", ProductListView.as_view(), name="catalog"),
    path("<slug:section_slug>/", ProductListView.as_view(), name="section"),
    path("<slug:section_slug>/<slug:subsection_slug>/", ProductListView.as_view(), name="subsection"),
    path("product/<slug:product_slug>", ProductDetailView.as_view(), name="product")
]