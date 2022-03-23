from django.shortcuts import render # метод для передачи шаблонов
from django.shortcuts import get_object_or_404 # функция для отображения при переходе на несуществующую страницу
from django.shortcuts import redirect # переадресация редирект 301 и 302
from django.http import HttpResponse # импортирую класс из библиотеки django
from django.http import HttpResponseNotFound # функция по обработке ошибки 404
from django.views.generic import DetailView # класс для отображения поста
from django.views.generic import CreateView # класс для работы с формами
from django.views.generic import ListView # для отображения главной страницы
from django.http import Http404 # ?

from .forms import * # импортировал все модели из файла forms.py
from .models import * # импортирует классы и функции из файла models.py
from django.urls import reverse, reverse_lazy # метод для перехода на страницу, когда это нужно

# Create your views here.

class WomenHome(ListView): # наследую атрибуты из класса ListView
    model = Women # атрибут для отображения модели Women
    template_name = 'women/index.html' # атрибут, который указывает путь к шаблону
    context_object_name = 'posts' # присвоил имя для атрибута, для отображения модели

    def get_context_data(self, *, object_list=None, **kwargs): # создал динамические данные для передачи в шаблон
        context = super().get_context_data(**kwargs) # **kwargs команда распаковывает словарь
        context['menu'] = menu # для ключа menu передаю переменную menu
        context['title'] = "Главная страница" # отображает названние страницы
        context['cat_selected'] = 0 # делает пункт меню выбранным
        return context # возвращаю context для отображения

    def get_queryset(self):
        return Women.objects.filter(is_published=True) # отображает статьи которые отмечены

# def index(request): # HttpRequest - поступает запрос от пользоваетя
#    posts = Women.objects.all() # показывает все статьи из таблицы SQL

#   context = { # добавил словарь чтобы все влазило на один экран
#      'posts': posts,
#       'menu': menu,
#       'title': 'Главная страница',
#       'cat_selected': 0, #
#   }
#   return render(request, 'women/index.html', context=context) # атрибут context - делает ссылку на словарь

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'about': 'О сайте'}) # добавил список в шаблон

# нужно внести изменение в файле urls.py
class AddPage(CreateView): # класс для работы с формами
    form_class = AddPostForm # атрибут обращается к классу AddPostForm
    template_name = 'women/addpage.html' # прописал адрес к шаблону
    success_url = reverse_lazy('home') # строит маршрут когда это надо

    def get_context_data(self, *, object_list=None, **kwargs):  # создал динамические данные для передачи в шаблон
        context = super().get_context_data(**kwargs)  # **kwargs команда распаковывает словарь
        context['menu'] = menu  # для ключа menu передаю переменную menu
        context['title'] = "Добавление статьи"  # отображает названние страницы
        return context  # возвращаю context для отображения

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES) # передадим список файлов, которые были переданы из формы
#         if form.is_valid(): # проверяет корректность данных и передачу на сервер
#             # print(form.cleaned_data) # отображаем в консоли очищенные данные
#             form.save() # генерирует автоматические сообщения об ошибке
#             return redirect('home') # если добавление прошло успешно делаем добавление на главную страницу
#
#
#     else:
#         form = AddPostForm() # добавил модель в шаблон addpage, формируется пустая форма
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'}) # добавил ссылку на класс

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def pageNotFound(request, exception): # exception - используется для обработки исключений
    return HttpResponseNotFound('<h1>Страница не найдена</h1>') # выводит сообщение, когда страница открыта с ошибкой

# класс нужно прописать в urls.py
class ShowPost(DetailView): # класс для отображения статей
    model = Women # присваиваю атрибуту модель Women
    template_name = 'women/post.html' # прописываю маршрут на шаблон
    slug_url_kwarg = 'post_slug' # присвоил имя атрибуту
    # pk_url_kwarg = 'post_pk' служит для отображения по id
    context_object_name = 'post' # задал имя для отображения в шаблоне

    def get_context_data(self, *, object_list=None, **kwargs): # создал динамические данные для передачи в шаблон
        context = super().get_context_data(**kwargs) # **kwargs команда распаковывает словарь
        context['title'] = context['post'] # отображает названние страницы
        context['menu'] = menu  # для ключа menu передаю переменную menu
        context['cat_selected'] = context['posts'][0].cat_id # делает пункт меню выбранным
        return context # возвращаю context для отображения

# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug) # если pk не найдена в классе Women генерируется функция ошибки
#
#     context = { # сформировал словарь с параметрами, который буду передовать шаблону
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id, # передаю номер выбранной рубрики из класса Women
#     }
#
#     return render(request, 'women/post.html', context=context)

class WomenCategory(ListView): # наследую атрибуты из класса ListView (отображает список)
    model = Women # передаю атрибуты модель Women
    template_name = 'women/index.html' # сделал ссылку на шаблон
    context_object_name = 'posts' # присвоил атрибуту имя
    allow_empty = False # выводит ошибку при не существующей странице (ошибка 404)

    def get_queryset(self): # отображение категории по слагу
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True) #

    def get_context_data(self, *, object_list=None, **kwargs): # создал динамические данные для передачи в шаблон
        context = super().get_context_data(**kwargs) # **kwargs команда распаковывает словарь
        context['title'] = "Категория - " + str(context['posts'][0].cat) # отображает названние страницы
        context['menu'] = menu  # для ключа menu передаю переменную menu
        context['cat_selected'] = context['posts'][0].cat_id # делает пункт меню выбранным
        return context # возвращаю context для отображения

# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id) # выбираем посты, которые соответствуют текущей рубрике
#
#     if len(posts) == 0:
#         raise Http404() # если категория не будет найдена, будет выводиться ошибка
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'women/index.html', context=context)