from django.db import models
from django.urls import reverse # Если вам нужно вернуть абсолютную ссылку

# Create your models here.

class Women(models.Model):
    title = models.CharField(max_length=255) # строковое поле для небольших записей, max_length - обязательный аргумент, дли строки
    content = models.TextField(blank=True) # используется для больших текстовых сообщений
    photo = models.ImageField(upload_to='photos/%y/%m/%d/') # служит для загрузки изображений
    time_create = models.DateTimeField(auto_now_add=True) # заполняет дату и время автоматически
    time_update = models.DateTimeField(auto_now=True) # заполняет дату и время при обновлении имеющейся информации
    is_published = models.BooleanField(default=True) # значение поля True or False
    # 'Category' - передаю класс, как строку, потому что он находиться ниже класса Women
    # models.PROTECT - запрещает удаление записи из первичной модели, если она используется во вторичной
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True) # null=True означает, что модель можно заполнять нулями

    def __str__(self):
        return self.title # в терминале ORM будет выводить строки с заголовками модели

    # формирует маршрут к конкретной записи
    def get_absolute_url(self): # self - ссылка на экземпляр класса Women
        # self.pk - можно взять любой атрибут модели, в данном примере берем идентификатор
        return reverse('post', kwargs={'post_id': self.pk}) # reverse - возвращает абсолютную ссылку, соответствующую указанному представлению
        # kwargs - словарь

class Category(models.Model): # создаю вторую модель Категории
    # max_length - максимальная длина символов 100, db_index - поле будет индексированно
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self): # этот метод возвращает имя класса Category
        return self.name