from django.apps import AppConfig


class WomenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'women'
    verbose_name = 'Выдающийеся личности' # поменял в панеле администратора заголовок импортированного класса Women
