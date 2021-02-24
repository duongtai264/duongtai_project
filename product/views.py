from django.shortcuts import render
from . models import WebTheme
from django.views.generic import ListView, DetailView

# Create your views here.
class ProductDetailView(DetailView):
    model = WebTheme 
    template_name = 'product/product_detail.html'