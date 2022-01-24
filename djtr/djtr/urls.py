"""djtr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # добавил метод include, который делает переадресацию

from women.views import * # импортирует все функции из файла views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')), # "" - ссылка на главную страницу, http://127.0.0.1:8000/
]

handler404 = pageNotFound # функция для обработки страницы сайта с ошибкой, функция находиться в views.py