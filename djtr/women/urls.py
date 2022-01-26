from django.urls import path
from django.urls import re_path # регулярные выражения

from .views import * # импортирую все функции представления из файла views

urlpatterns = [
    path('', index, name='home'), # присвоил имя главной странице
    path('about', about, name='about') # прописал путь к странице о нас
]

