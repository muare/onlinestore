from django.db import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse

from .models import Manufacturer, Product
# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"


def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values("pk", "name"))}
    return JsonResponse(data)


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
            "name": product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.description,
            "url": product.photo.url,
            "price": product.price,
            "shipping_price": product.shipping_price,
            "quantity": product.quantity,
        }}
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({
            "error": {
                "code": 404,
                "message": "product not found",
            }
        }, status=404)


def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        products = manufacturer.products.all()
        data = {"manufacturer": {
            "name": manufacturer.name,
            "location": manufacturer.location,
            "activte": manufacturer.active,
            "products": list(products.values()),
        }}
        return JsonResponse(data)

    except Manufacturer.DoesNotExist:
        return JsonResponse({
            "error": {
                "code": 404,
                "message": "product not found",
            }
        }, status=404)


def manufacturer_list(request):
    try:
        manufacturers = Manufacturer.objects.filter(active=True)
        data = {"manufacturers": list(manufacturers.values())}

        return JsonResponse(data)

    except Manufacturer.DoesNotExist:
        return JsonResponse({
            "error": {
                "code": 404,
                "message": "product not found",
            }
        }, status=404)
