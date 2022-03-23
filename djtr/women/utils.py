# создал список состоящий из словаря
menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
]

#
class DataMixin:
        def get_user_context(self, **kwargs): # метод формирует нужный контекст по умолчанию
                context = kwargs # создал словарь из именнованых параметров, которые были переданы функции
                cats = Category.objects.all() #
                context['menu'] = menu #
                context['cats'] = cats #
                if 'cat_selected' not in context: #
                        context['cat_selected'] = 0 #
                return context #