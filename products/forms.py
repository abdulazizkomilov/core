from django.forms import ModelForm
from .models import Product, ProductImage, Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'address', 'zipcode', 'city',)

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price',)

class ImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ('product', 'image',)
