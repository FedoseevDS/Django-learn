from django.contrib import admin
from .models import * # импортирую все модели из файла models.py

# Register your models here.

class WomenAdmin(admin.ModelAdmin): # название класса совпадает с названием класса
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published') # прописываем поля, которые хотим видеть
    list_display_links = ('id', 'title') # создал переход по названию поля
    search_fields = ('title', 'content') # по каким полям можно будет производить поиск информации
    list_editable = ('is_published',) # делает поле редактированным
    list_filter = ('is_published', 'time_create') # фильт заданных полей

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # прописываем поля, которые хотим видеть
    list_display_links = ('id', 'name')  # создал переход по названию поля
    search_fields = ('name',)  # если один элемент, обязательно нужно поставить ,

admin.site.register(Women, WomenAdmin) # добавил 2 класс для отображения в панеле администратора
admin.site.register(Category, CategoryAdmin) # зарегистрировал класс Category в панеле администратора
