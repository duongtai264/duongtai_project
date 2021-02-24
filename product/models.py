from django.db import models
from django.contrib.auth.models import User

class CategoryProduct(models.Model):
    name        = models.TextField()
    code        = models.IntegerField()
    avatar      = models.ImageField()
    
    def __str__(self):
        return self.name

class CategoryBlog(models.Model):
    name        = models.TextField()
    code        = models.IntegerField()
    avatar      = models.ImageField()
    
    def __str__(self):
        return str(self.id) + ' | '+ self.name
    
class WebTheme(models.Model):
    code        = models.IntegerField()
    name        = models.TextField()
    content     = models.TextField()
    category    = models.ForeignKey(CategoryProduct, on_delete=models.SET_DEFAULT, default=1)
    description = models.TextField()
    active      = models.BooleanField(default=1)
    image      = models.ImageField()
    price      = models.FloatField()

    def __str__(self):
        return str(self.id) + ' | '+ self.name    
    
class Blog(models.Model):
    title       = models.TextField()
    description = models.TextField()
    content     = models.TextField()
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime    = models.DateField(auto_now_add=True)
    category    = models.ForeignKey(CategoryBlog, on_delete=models.SET_DEFAULT, default=1)
    active      = models.BooleanField(default=1)
    avatar      = models.ImageField()
    
    def __str__(self):
        return str(self.id) + ' | '+ self.title