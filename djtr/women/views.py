from django.shortcuts import render # метод для передачи шаблонов
from django.shortcuts import get_object_or_404 # функция для отображения при переходе на несуществующую страницу
from django.shortcuts import redirect # переадресация редирект 301 и 302
from django.http import HttpResponse # импортирую класс из библиотеки django
from django.http import HttpResponseNotFound # функция по обработке ошибки 404
from django.http import Http404 # ?

from .forms import * # импортировал все модели из файла forms.py
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

    context = { # добавил словарь чтобы все влазило на один экран
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0, #
    }
    return render(request, 'women/index.html', context=context) # атрибут context - делает ссылку на словарь

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'about': 'О сайте'}) # добавил список в шаблон

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST) # форма с заполненными данными
        if form.is_valid(): # проверяет корректность данных и передачу на сервер
            # print(form.cleaned_data) # отображаем в консоли очищенные данные
            try: #
                Women.objects.create(**form.cleaned_data) # делаем добавление новой записи в базу данных
                return redirect('home') # если добавление прошло успешно делаем добавление на главную страницу
            except: #
                form.add_error(None, 'Ошибка добавления поста') # если произошла ошибка, отображаем ее на странице формы

    else:
        form = AddPostForm() # добавил модель в шаблон addpage, формируется пустая форма
    return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'}) # добавил ссылку на класс

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def pageNotFound(request, exception): # exception - используется для обработки исключений
    return HttpResponseNotFound('<h1>Страница не найдена</h1>') # выводит сообщение, когда страница открыта с ошибкой

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug) # если pk не найдена в классе Women генерируется функция ошибки

    context = { # сформировал словарь с параметрами, который буду передовать шаблону
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id, # передаю номер выбранной рубрики из класса Women
    }

    return render(request, 'women/post.html', context=context)

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id) # выбираем посты, которые соответствуют текущей рубрике

    if len(posts) == 0:
        raise Http404() # если категория не будет найдена, будет выводиться ошибка

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)