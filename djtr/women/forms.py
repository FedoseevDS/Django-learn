from django import forms # импортирую модель формс из джанго
from django.core.exceptions import ValidationError # добавил класс валидации

from .models import * # импортирую модели из файла models.py

class AddPostForm (forms.ModelForm): # наследует класс ModelForm
    def __init__(self, *args, **kwargs): # вызывается конструктор
        super().__init__(*args, **kwargs) # вызывает конструктор базового класса ModelForm
        self.fields['cat'].empty_label = 'Категория не выбрана' # поменял имя для атрибута cat

    class Meta:
        model = Women # создает связь с классом Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat'] # добавил поле фото
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}), # присвоил класс для поля
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}), # присвоил 60 колонок и 10 строчек
        }

    def clean_title(self): # clean - обязательное название title - название атрибута
        title = self.cleaned_data['title'] #
        if len(title) > 200: # условие, если длинна заголовка > 200
            raise ValidationError('Длина превышает 200 символов') # генерируется исключение

        return title # иначе возвращается заголовок
