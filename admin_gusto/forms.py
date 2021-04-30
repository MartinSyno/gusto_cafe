from django import forms
from main_gusto.models import Category, Dish

class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=15,
                                widget=forms.TextInput(attrs={"placeholder": "Название категории", "required": "required"}))

    photo = forms.ImageField(widget=forms.FileInput())

    category_order = forms.IntegerField(
        widget=forms.TextInput(attrs={"placeholder": "Порядок категории в меню", "required": "required"}))

    is_visible = forms.BooleanField(initial=True, required=False)

    class Meta():
        model = Category
        fields = ("title", "photo", "category_order", "is_visible")

class DishForm(forms.ModelForm):
    title = forms.CharField(max_length=25,
                                widget=forms.TextInput(attrs={"placeholder": "Название блюда", "required": "required"}))

    photo = forms.ImageField(widget=forms.FileInput())

    dish_order = forms.IntegerField(
        widget=forms.NumberInput(attrs={"placeholder": "Порядок блюда в категории", "required": "required"}))

    is_visible = forms.BooleanField(initial=True, required=False)

    class Meta():
        model = Dish
        fields = ("title", "slug", "photo", "dish_order", "is_visible", "price", "available", "desc", "category")
        #exclude = ['slug'] #Чтобы slug вводился автоматически и в формах.