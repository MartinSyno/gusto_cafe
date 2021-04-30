from django.urls import path
from .views import main_page_view, dish_page_view

app_name = "main_gusto"

urlpatterns = [
    path("", main_page_view, name="main_page_view"),
    path("menu/dish/<int:id>/<slug:slug>", dish_page_view, name="dish_page_view"),
]