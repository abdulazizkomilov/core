from django.contrib import admin
from .models import Category, Product, Comment, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'slug', 'created_at', 'category', 'user']
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
admin.site.register(ProductImage)
