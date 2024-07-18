from django.contrib import admin
from .models import Category, Product, Brand, ProductLine,ProductImage


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(ProductLine)
admin.site.register(ProductImage)
