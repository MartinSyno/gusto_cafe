from django.db import models
from uuid import uuid4
from os import path
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split(".")[-1]
        filename = f"{uuid4()}.{ext}"
        return path.join("images/categories", filename)

    title = models.CharField(max_length=15, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    category_order = models.IntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}: {self.category_order}"

class Dish(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split(".")[-1]  # Узнать разширение файла (my_photo.jpg -> [ "my_photo", "jpg" ])
        filename = f"{uuid4()}.{ext}"
        return path.join("images/dishes", filename)

    title = models.CharField(max_length=25, unique=True, db_index=True)
    slug = models.SlugField(db_index=True)
    photo = models.ImageField(upload_to=get_file_name)  # upload_to='products/%Y/%m/%d'
    dish_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    desc = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.hiring)
    #     super(hire_article, self).save(*args, **kwargs) #Чтобы slug вводился автоматически и в формах.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main_gusto:dish_page_view", args=[self.id, self.slug])

class Info(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split(".")[-1]  # Узнать разширение файла (my_photo.jpg -> [ "my_photo", "jpg" ])
        filename = f"{uuid4()}.{ext}"
        return path.join("images/info", filename)

    cafe_info = models.CharField(max_length=500, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

class Team(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split(".")[-1]  # Узнать разширение файла (my_photo.jpg -> [ "my_photo", "jpg" ])
        filename = f"{uuid4()}.{ext}"
        return path.join("images/team", filename)

    team_info = models.CharField(max_length=500, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

class Phone(models.Model):
    phone = models.CharField(max_length=13, unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.phone}"

class Adress(models.Model):
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    home = models.CharField(max_length=5)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.city}; {self.street}; {self.home}"

class OpeningHours(models.Model):
    day = models.CharField(max_length=10)
    hours_start = models.CharField(max_length=5)
    hours_end = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.day} - {self.hours_start}-{self.hours_end}"

class CafeInfo(models.Model):
    adress_id = models.ForeignKey(Adress, on_delete=models.CASCADE)
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE)
    openinghours_id = models.ForeignKey(OpeningHours, on_delete=models.CASCADE)


class Message(models.Model):
    user_name = models.CharField(max_length=40)
    user_email = models.EmailField()
    user_message = models.CharField(max_length=400)

    pub_date = models.DateField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_name} : {self.user_email} : {self.user_message[:20]}"