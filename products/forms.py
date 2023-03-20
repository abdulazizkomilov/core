from django.forms import ModelForm
from .models import Product, ProductImage

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price',)

class ImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ('product', 'image',)
