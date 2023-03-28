from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from products.models import Product
from django.contrib.auth import login
from .models import Userprofile

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = Userprofile.objects.create(user=user)
            messages.success(request, 'Your accounts succesfully created.')
            return redirect('/accounts')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/signup.html', {
        'form': form
    })


def vendor_detail(request, pk):

    user = User.objects.get(pk=pk)
    products = user.products.filter(status=Product.ACTIVE)

    return render(request, 'users/vendor_detail.html', {
        'user': user, 
        'products': products,
    })
