from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
#admin.site.register(Dish)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'available', 'created', 'updated']#['title', 'slug', "photo", "dish_order", "is_visible", 'price', 'available', "desc", "category", 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Phone)
admin.site.register(Adress)
admin.site.register(Team)
admin.site.register(Info)
admin.site.register(OpeningHours)
admin.site.register(Message)
admin.site.register(CafeInfo)