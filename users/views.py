from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib import messages
from .models import Userprofile
from products.models import Product
from django.contrib.auth import login
from .models import Userprofile

class SignUpView(View):
    def get(self, request):
        return render(request, 'registration/signup.html', {'form':UserCreationForm()})
    
    def post(self, request):
        form = UserCreationForm(data=request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account successfully created.')
            return redirect('login')
        return render(request, 'registration/signup.html', {'form':form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = Userprofile.objects.create(user=user)
            messages.success(request, 'Your account successfully created.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form':form})

def vendor_detail(request, pk):

    user = Userprofile.objects.get(pk=pk)
    products = user.products.filter(status=Product.ACTIVE)

    return render(request, 'users/vendor_detail.html', {
        'user': user, 
        'products': products,
    })
