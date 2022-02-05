from django.shortcuts import render # метод для передачи шаблонов
from django.shortcuts import redirect # переадресация редирект 301 и 302
from django.http import HttpResponse # импортирую класс из библиотеки django
from django.http import HttpResponseNotFound # функция по обработке ошибки 404
from django.http import Http404 # ?
from .models import * # импортирует классы и функции из файла models.py
from django.urls import reverse

# Create your views here.

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
] # добавил список ввиде словарей

def index(request): # HttpRequest - поступает запрос от пользоваетя
    posts = Women.objects.all() # показывает все статьи из таблицы SQL
    cats = Category.objects.all() # показывает категории из SQL

    context = { # добавил словарь чтобы все влазило на один экран
        'posts': posts,
        'cats': cats, #
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0, #
    }
    return render(request, 'women/index.html', context=context) # атрибут context - делает ссылку на словарь

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'about': 'О сайте'}) # добавил список в шаблон

def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def pageNotFound(request, exception): # exception - используется для обработки исключений
    return HttpResponseNotFound('<h1>Страница не найдена</h1>') # выводит сообщение, когда страница открыта с ошибкой

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}') # добавил представления для постов

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id) # выбираем посты, которые соответствуют текущей рубрике
    cats = Category.objects.all() # выбираем рубрики для отображения на странице

    if len(posts) == 0:
        raise Http404() # если категория не будет найдена, будет выводиться ошибка

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context) #