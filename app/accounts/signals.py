from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# Сигнал для создания профиля при создании пользователя
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        # Заполнение slug, если оно пустое
        if not profile.slug:
            profile.slug = instance.username  # или другая логика для slug
            profile.save()

# Сигнал для сохранения профиля
@receiver(post_save, sender=Profile)
def save_user_profile(sender, instance, **kwargs):
    # Добавляем проверку, чтобы избежать рекурсии
    if not instance._state.adding:  # Проверяем, что профиль уже существует
        return
    instance.save()
