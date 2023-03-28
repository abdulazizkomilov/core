from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import resolve
from django.views import View
from products.models import Product, Category, ProductImage, Order, OrderItem
from django.db.models import Q
from products.forms import ProductForm, ImageForm, OrderForm
from django.utils.text import slugify
from django.contrib import messages
from .cart import Cart



def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('store:cart_view')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect('store:cart_view')

def change_quantity(request, product_id):

    action = request.GET.get('action', '')

    quantity = 1

    if action == 'decrease':
        quantity =- 1
    
    cart = Cart(request)
    cart.add(product_id, quantity, True)

    return redirect('store:cart_view')


def cart_view(request):
    cart = Cart(request)

    context = {
        'cart': cart,
    }

    return render(request, 'product/cart_view.html', context)

@login_required
def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            total_price = 0

            for item in cart:
                product = item['product']
                total_price += product.price * int(item['quantity'])

            order = form.save(commit=False)
            order.created_by = request.user
            order.paid_amount = total_price
            order.save()

            for item in cart:
                product = item['product']
                quantity = int(item['quantity'])
                price = product.price * quantity

                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

            cart.clear()

            return redirect('store:accounts')
    else:
        form = OrderForm()

    context = {
        'cart': cart,
        'form': form,
    }

    return render(request, 'registration/checkout.html', context)


def for_all_pages(request):
    categories = Category.objects.all()
    return {"categories":categories}

def page_name(request):
    url_name = resolve(request.path).url_name
    return {'url_name': url_name}

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(status=Product.ACTIVE).filter(Q(title__icontains=query) | Q(description__icontains=query))

    context = {
        'query': query,
        'products': products,
    }

    return render(request, 'product/search.html', context)

class IndexView(View):
    def get(self, request):
        categories_all = Category.objects.all()
        products = Product.objects.filter(status=Product.ACTIVE)

        cart = Cart(request)

        context = {
            'categories_all': categories_all,
            'products': products,
            'cart': cart,
        }

        return render(request, 'storepage.html', context)


class CategoryView(View):
    def get(self, request, category_name):
        category = get_object_or_404(Category, title=category_name)
        products = Product.objects.filter(status=Product.ACTIVE).filter(category=category)

        context = {
            'category': category,
            'products': products,
        }

        return render(request, 'product/category.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)
    
    context = {
            'product': product,
        }

    return render(request, 'product/product_detail.html', context)


@login_required
def accounts(request):
    products = request.user.products.exclude(status=Product.DELETED)

    context = {
        'products': products
    }
    return render(request, 'users/accounts.html', context)

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            messages.success(request, 'The Product was added!')

            return redirect('store:accounts')

    else:
        form = ProductForm()

    context = {
        'title': 'Add product',
        'form': form,
    }
    return render(request, 'product/add_product.html', context)


@login_required
def add_product_img(request):
    if request.method == 'POST':
        form_img = ImageForm(request.POST, request.FILES)

        if form_img.is_valid():
            product = form_img.save(commit=False)
            product.user = request.user
            product.save()

            messages.success(request, 'The Image for Product was added!')

            return redirect('store:accounts')

    else:
        form_img = ImageForm()

    context = {
        'title': 'Add image product',
        'form_img': form_img,
    }
    return render(request, 'product/add_product.html', context)



@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        form_img = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form_img.save()

            messages.success(request, 'The Change was saved!')

            return redirect('store:accounts')
        

    else:
        form = ProductForm(instance=product)
        form_img = ImageForm()
        
    context = {
        'title': 'Edit product',
        'product': product,
        'form': form,
        'form_img': form_img,
    }
    return render(request, 'product/add_product.html', context)


@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()

    messages.success(request, 'The Product was deleted!')

    return redirect('store:accounts')



















def justpage(request):
    return render(request, 'justpage.html')

def homepage(request):
    return render(request, 'home.html')



