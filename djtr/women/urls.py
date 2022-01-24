from django.urls import path
from django.urls import re_path # регулярные выражения

from .views import * # импортирую все функции представления из файла views

urlpatterns = [
    path('', index, name='home'), # присвоил имя главной странице
    path('cats/<int:catid>/', categories), # показывает номера, слова категории при открытие страницы
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive), # archive - префикс, (?P<year>[0-9]{4}) - выводит год
]

