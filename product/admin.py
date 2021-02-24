from django.contrib import admin
from .models import WebTheme, Blog, CategoryBlog, CategoryProduct

class Category_Blog(admin.ModelAdmin):
    list_display = ('id', 'name','avatar')
admin.site.register(CategoryBlog, Category_Blog)

class Category_Product(admin.ModelAdmin):
    list_display = ('id', 'name','avatar')
admin.site.register(CategoryProduct, Category_Product)

class Web_Theme(admin.ModelAdmin):
    list_display = ('id', 'name','category', 'description', 'price', 'active')
admin.site.register(WebTheme, Web_Theme)

class Post(admin.ModelAdmin):
    list_display = ('id','title','author', 'category', 'description', 'datetime')
admin.site.register(Blog, Post)