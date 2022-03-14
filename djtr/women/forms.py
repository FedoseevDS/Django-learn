from django import forms # импортирую модель формс из джанго
from .models import * # импортирую модели из файла models.py

class AddPostForm (forms.Form): # название придумываем сами
    title = forms.CharField(max_length=255) # атрибут заголовок, длина 255 символов
    slug = forms.SlugField(max_length=255) # слаг, длина 255 символов
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10})) #
    is_published = forms.BooleanField() # делаем разрешение опубликовано/не опубликовано
    cat = forms.ModelChoiceField(queryset=Category.objects.all()) # дает при публикации выбрать категорию