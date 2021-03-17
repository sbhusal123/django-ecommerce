from django.contrib import admin

from .models import Product, DealProduct, Attributes, ProductImage, ProductAttributes, Deal, Category

admin.site.register([Product, Attributes, ProductImage, DealProduct, Deal, Category])


@admin.register(ProductAttributes)
class ProductAttributesAdmin(admin.ModelAdmin):
    pass
