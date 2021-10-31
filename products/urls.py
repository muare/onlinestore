from django.urls import path
from .views import ProductListView, ProductDetailView
from .views import product_list, product_detail, manufacturer_detail, manufacturer_list

urlpatterns = [
    # path("products/", ProductListView.as_view(), name="product-list"),
    # path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>/", product_detail, name="product-detail"),
    path("manufacturers/<int:pk>/", manufacturer_detail, name="manufacturer-detail"),
    path("manufacturers/", manufacturer_list, name="manufacturer-list"),
]
