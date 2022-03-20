from django.db import models
from django.urls import reverse # Если вам нужно вернуть абсолютную ссылку

# Create your models here.

class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок') # добавил названия отображения поля
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL') # добавил параметр для отображения slug
    content = models.TextField(blank=True, verbose_name='Текст статьи') #
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', verbose_name='Фото') #
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания') #
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения') #
    is_published = models.BooleanField(default=True, verbose_name='Публикация') #
    # 'Category' - передаю класс, как строку, потому что он находиться ниже класса Women
    # models.PROTECT - запрещает удаление записи из первичной модели, если она используется во вторичной
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, ) #

    def __str__(self):
        return self.title # в терминале ORM будет выводить строки с заголовками модели

    # формирует маршрут к конкретной записи
    def get_absolute_url(self): # self - ссылка на экземпляр класса Women
        # self.pk - можно взять любой атрибут модели, в данном примере берем идентификатор
        return reverse('post', kwargs={'post_slug': self.slug}) # reverse - возвращает абсолютную ссылку, соответствующую указанному представлению
        # kwargs - словарь

    class Meta: # переименовывает добавленный класс в панель администратора
        verbose_name = 'Известные личности' # на конце если множественное число появляется буква s
        verbose_name_plural = 'Известные личности' # убираем букву s
        ordering = ['time_create', 'title'] # порядок сортировки постов, можно задать несколько параметров

class Category(models.Model): # создаю вторую модель Категории
    # max_length - максимальная длина символов 100, db_index - поле будет индексированно
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL') # добавил параметр для отображения slug

    def __str__(self): # этот метод возвращает имя класса Category
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['id']