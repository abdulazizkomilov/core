from django.urls import path
from .views import signup, vendor_detail

app_name = 'users'

urlpatterns = [
    path('vendors/<int:pk>', vendor_detail, name='vendor_detail'),
    path('signup/', signup, name='signup'),
]

