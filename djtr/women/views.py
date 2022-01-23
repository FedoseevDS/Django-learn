from django.shortcuts import render
from django.http import HttpResponse # импортирую класс из библиотеки django

# Create your views here.

def index(request): # HttpRequest - поступает запрос от пользоваетя
    return HttpResponse('Страница приложения women.') # поступает ответ от сервера к пользователю

def categories(request):
    return HttpResponse('<h1>Статьи по категориям</h1>') # создал дополнительное представление