#app/accounts/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from app.services.utils import unique_slugify
from django.utils import timezone
from django.core.cache import cache
from django.conf import settings

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, verbose_name='URL', max_length=255, blank=True)
    bio = models.TextField(max_length=500, verbose_name='Информация о себе', blank=True)
    avatar = models.ImageField(verbose_name='Аватар', upload_to='images/avatars/%Y/%m/%d/',
        default='images/avatars/default.png',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    class Meta:
        """
        Сортировка , название таблицы в базе данных
        """
        ordering = ['user',]
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def save(self, *args, **kwargs):
        """
        Добавляем проверку на наличие slug и избегаем рекурсии.
        """
        if not self.slug:  # Если slug еще не был установлен
            self.slug = unique_slugify(self, self.user.username, self.slug)
        # Проверка, если slug уже установлен, не вызываем save повторно
        if not self.pk:
            super().save(*args, **kwargs)
        else:
            super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        """
        Возвращение строки 
        """
        return self.user.username
    
    def get_absolute_url(self):
        """
        Ссылка на профиль
        """
        return reverse("accounts:profile_detail", kwargs={"slug": self.slug})
