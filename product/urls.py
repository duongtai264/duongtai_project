from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
urlpatterns = [
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product'), 
]
