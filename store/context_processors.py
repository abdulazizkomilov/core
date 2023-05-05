from store.cart import Cart

def cart(request):
    return {'cart': Cart}