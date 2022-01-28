from django.shortcuts import render # метод для передачи шаблонов
from django.shortcuts import redirect # переадресация редирект 301 и 302
from django.http import HttpResponse # импортирую класс из библиотеки django
from django.http import HttpResponseNotFound # функция по обработке ошибки 404
from django.http import Http404 # ?

# Create your views here.

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти', 'Баракуда']

def index(request): # HttpRequest - поступает запрос от пользоваетя
    return render(request, 'women/index.html', {'menu': menu, 'title': 'Главная страница'}) # добавил список в словарь

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'about': 'О сайте'}) # добавил список в шаблон

def categories(request, catid): # добавил 2 атрибут который будет показывать номер категории
    if request.GET: # условие если в GET есть данные то
         print(request.GET) # выводится значение

    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>') # добавил <p> который будет показывать № категории

def archive(request, year): # добавил атрибут года
    if int(year) > 2020: # условие если год выше 2020
        return redirect('home', permanent=True) # переадресация на страницу home. редирект 301 - постоянный

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>') # в префиксе страницы будет отображаться год

def pageNotFound(request, exception): # exception - используется для обработки исключений
    return HttpResponseNotFound('<h1>Страница не найдена</h1>') # выводит сообщение, когда страница открыта с ошибкой