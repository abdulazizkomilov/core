from django.urls import path
from .views import *

app_name = 'store'

urlpatterns = [
    path('store/<slug:slug>/', product_detail, name='product_detail'),
    path('search/', search, name='search'),
    path('', homepage, name='home'),
    path('cart/checkout/', checkout, name='checkout'),
    path('page/', justpage, name='page'),
    path('store/', IndexView.as_view(), name='store'),
    path('store/add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/change-quantity/<str:product_id>/', change_quantity, name='change_quantity'),
    path('cart/<str:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', cart_view, name='cart_view'),
    path('store/<str:category_name>/category', CategoryView.as_view(), name='category'),
    path('accounts/edit-product/<int:pk>/', edit_product, name='edit_product'),
    path('accounts/add-product/', add_product, name='add_product'),
    path('accounts/add-product-img/', add_product_img, name='add_product_img'),
    path('accounts/delete-product/<int:pk>/', delete_product, name='delete_product'),
    path('accounts/', accounts, name='accounts'),
]


