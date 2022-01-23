from django.urls import path

from .views import * # импортирую все функции представления из файла views

urlpatterns = [
    path('', index), # прописываем все маршруты текущего приложения
    path('cats/', categories), # добавил дополнительную страницу http://127.0.0.1:8000/cats/
]

