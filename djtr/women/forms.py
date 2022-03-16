from django import forms # импортирую модель формс из джанго
from .models import * # импортирую модели из файла models.py

class AddPostForm (forms.Form): # название придумываем сами
    title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # widget - позволяет добавить стиль к конкретному полю формы
    slug = forms.SlugField(max_length=255, label='URL') # Label - переименовывает название
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Текст') # Label - переименовывает название
    is_published = forms.BooleanField(label='Публикация', required=False, initial=True)
    # required - делает атрибут не обязательным initial - ставит значение по умолчанию
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Ктегории', empty_label='Категория не выбрана')
    # empty_label - значение по умолчанию