from django import forms
from .models import Post, Comment
from django.utils.text import slugify

class PostCreateForm(forms.ModelForm):
    """
    Форма добавления статей на сайт
    """
    class Meta:
        model = Post
        fields = ('title', 'content', 'status' )  # Убрали 'slug'

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def save(self, commit=True):
        """
        Переопределение метода save для автоматической генерации slug
        """
        instance = super().save(commit=False)
        if not instance.slug:  # Проверяем, если slug не задан
            base_slug = slugify(instance.title)
            unique_slug = base_slug
            counter = 1
            # Проверяем уникальность slug, добавляя счетчик при необходимости
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            instance.slug = unique_slug

        if commit:
            instance.save()
        return instance


class PostUpdateForm(forms.ModelForm):
    """
    Форма обновления статей на сайте
    """
    class Meta:
        model = Post
        fields = ('title', 'content', 'status')  # Убрали 'slug'

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def save(self, commit=True):
        """
        Сохраняем обновленный slug только если title изменен
        """
        instance = super().save(commit=False)
        if not instance.slug or instance.slug != slugify(instance.title):
            base_slug = slugify(instance.title)
            unique_slug = base_slug
            counter = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            instance.slug = unique_slug

        if commit:
            instance.save()
        return instance

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Напишите ваш комментарий...'
            }),
        }
        labels = {
            'content': ''
        }

