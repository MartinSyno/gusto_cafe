from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import FormMessage
from cart.cart import Cart#

# Create your views here.
def main_page_view(request):

    if request.method == "POST":
        form = FormMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")


    categories = Category.objects.filter(is_visible=True).order_by("category_order")
    for item in categories:
        dishes = Dish.objects.filter(category=item.pk).filter(is_visible=True).order_by("dish_order")
        item.dishes = dishes
    special = Dish.objects.filter(category__title="Меню от шефа")

    team_info = Team.objects.filter(is_visible=True)
    cafe_info = Info.objects.filter(is_visible=True)
    phone = Phone.objects.filter(is_visible=True)
    adress = Adress.objects.filter(is_visible=True)
    opening_hours = OpeningHours.objects.all()

    form = FormMessage()

    cart = Cart(request)#

    return render(request, "index.html", context={
        "categories": categories,
        "special": special,
        "team_info": team_info[0],
        "cafe_info": cafe_info[0],
        "phone": phone,
        "adress": adress,
        "opening_hours": opening_hours,
        "form": form,
        "cart": cart,#
    })


def dish_page_view(request, id, slug):
    dish = get_object_or_404(Dish, id=id, slug=slug)#, available=True)
    cart = Cart(request)
    return render(request, "dish_info.html", context={'dish': dish, 'cart': cart})#