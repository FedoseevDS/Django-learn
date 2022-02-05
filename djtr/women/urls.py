from django.urls import path
from django.urls import re_path # регулярные выражения
from django.urls import reverse

from .views import * # импортирую все функции представления из файла views

urlpatterns = [
    path('', index, name='home'), # присвоил имя главной странице
    path('about/', about, name='about'), # прописал путь к странице о нас
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'), # добавил ссылку на пост
    path('category/<int:cat_id>/', show_category, name='category'), # добавил ссылку на категории
]

