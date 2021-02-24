from django.shortcuts import render
from django.http import HttpResponse
from product.models import CategoryProduct, CategoryBlog, WebTheme, Blog

def index(request, *args, **kwargs):
    data = {'Product' : WebTheme.objects.all().order_by("-id")}
    return render(request, 'pages/home.html',data)

def product_page(request, *args, **kwargs):
    
    return render(request, 'pages/product_page.html', {})


def blog_page(request, *args, **kwargs):
    
    return render(request, 'pages/blog_page.html', {})


def about(request, *args, **kwargs):
    
    return render(request, 'pages/about.html', {})


def contact(request, *args, **kwargs):
    
    return render(request, 'pages/contact.html', {})
