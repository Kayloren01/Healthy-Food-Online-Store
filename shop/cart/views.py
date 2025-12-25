from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def card_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])

    product_id_str = str(product.id)
    if product_id_str in cart.cart:
        if cart.cart[product_id_str]['quantity'] <= 0:
            cart.remove(product)
    return redirect('cart:cart_detail')


def card_minus(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.minus(product=product, quantity=cd['quantity'], override_quantity=cd['override'])

    product_id_str = str(product.id)
    if product_id_str in cart.cart:
        if cart.cart[product_id_str]['quantity'] <= 0:
            cart.remove(product)
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


@require_POST
def all_remove(request):
    cart = Cart(request)
    for item in cart:
        print(item)
        cart.remove(item['product'])
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)

    items_to_remove = []
    for item in cart:
        if item['quantity'] <= 0:
            items_to_remove.append(item['product'])
    
    # Удаляем товары с количеством ≤ 0
    for product in items_to_remove:
        cart.remove(product)
    cart_product_form = CartAddProductForm()
    for item in cart:
       
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
    return render(request, 'cart_detail.html', {'cart': cart, 'cart_product_form': cart_product_form})
