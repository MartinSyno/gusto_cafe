from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:dish_id>', cart_add, name='cart_add'),
    path('remove/<int:dish_id>', cart_remove, name='cart_remove'),
]