from django.urls import path
from django.urls import re_path # регулярные выражения
from django.urls import reverse

from .views import * # импортирую все функции представления из файла views

urlpatterns = [
    path('', WomenHome.as_view(), name='home'), # присвоил имя главной странице
    path('about/', about, name='about'), # прописал путь к странице о нас
    path('addpage/', AddPage.as_view(), name='add_page'), # подключил класс AddPage, as.view() - обязательный метод
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'), # добавил класс из файла views.py
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'), # ссылка на категорию по слагу
]

