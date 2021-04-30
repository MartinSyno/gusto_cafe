from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET

from main_gusto.models import Dish

from .cart import Cart

# Create your views here.

@require_GET
def cart_add(request, dish_id):
    cart = Cart(request)
    dish = get_object_or_404(Dish, id=dish_id)
    cart.add(dish=dish, quantity=1)
    return redirect('cart:cart_detail')

def cart_remove(request, dish_id):
    cart = Cart(request)
    dish = get_object_or_404(Dish, id=dish_id)
    cart.remove(dish)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})
