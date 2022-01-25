from django.db import models

# Create your models here.

class Women(models.Model):
    title = models.CharField(max_length=255) # строковое поле для небольших записей, max_length - обязательный аргумент, дли строки
    content = models.TextField(blank=True) # используется для больших текстовых сообщений
    photo = models.ImageField(upload_to='photos/%y/%m/%d/') # служит для загрузки изображений
    time_create = models.DateTimeField(auto_now_add=True) # заполняет дату и время автоматически
    time_update = models.DateTimeField(auto_now=True) # заполняет дату и время при обновлении имеющейся информации
    is_published = models.BooleanField(default=True) # значение поля True or False

    def __str__(self):
        return self.title # в терминале ORM будет выводить строки с заголовками модели

