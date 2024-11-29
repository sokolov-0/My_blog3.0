from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.conf import settings



class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Наименование категории')
    slug = models.SlugField(unique=True, allow_unicode=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Категория'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class PostManager(models.Manager):
    """
    Кастомный менеджер для модели постов
    """
    def get_queryset(self):
        """
        Список постов(sql запросы с фильтрацией по стататусу опубликованные )
        """
        return super().get_queryset().select_related('author').filter(status='published')#добавть после автора категорию если добавлю вооюще категории



class Post(models.Model):
    """
    Модель постов для блога
    """
    STATUS_OPTIONS = (
        ('published', 'Опубликовано'),
        ('draft', 'Черновик')
    )
    title = models.CharField(max_length=300, verbose_name='Название записи')
    slug = models.SlugField( verbose_name='URL', blank=True, unique=True)
    content = models.TextField(verbose_name='Основной текст стаьи')
    created = models.DateTimeField(verbose_name='Дата и время создания поста', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата и время обновления поста', auto_now=True)
    status = models.CharField(choices=STATUS_OPTIONS, default='published', verbose_name='Статус записи', max_length=10)
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_posts')
    updater = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='updater_posts')
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
    class Meta:
        db_table = 'blog_post'
        ordering = ['-created']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """
        Переопределение метода save для автоматической генерации уникального slug.
        """
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            # Проверяем, существует ли уже запись с таким slug
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    objects = PostManager()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий от {self.user.username} к {self.post.title}'
    

