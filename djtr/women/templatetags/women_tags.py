from django import template  # библиотека для работы с шаблонами
from women.models import *  # созданные классы

register = template.Library()  # создаю экземлпяр через который происходит регистрация всех шаблонов


@register.simple_tag(name='getcats')  # присвоил имя функции с помощью атрибута name
def get_categories(filter=None): # простой тег, добавил фильтр, как дополнительный параметр
    if not filter: # если фильтр имеет значение None
        return Category.objects.all() # выбираем все что есть в категориях
    else:
        return Category.objects.filter(pk=filter) # выбирает pk по записи фильтра

@register.inclusion_tag('women/list_categories.html') # включающий тег
def show_categories(sort=None, cat_selected=0): # добавил 2 параметра
    if not sort:
        cats = Category.objects.all() # выбираем все если сортировка не определена
    else:
        cats = Category.objects.order_by(sort) # если определена делаем сортировку по указаному полю

    return {'cats': cats, 'cat_selected': cat_selected} # 2 параметр находится в list_categories.html