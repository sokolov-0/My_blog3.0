from django.shortcuts import render,get_object_or_404, redirect

from .models import Post, Comment, Category, Tag
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .forms import PostCreateForm, PostUpdateForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.http import HttpResponseForbidden

class PostListView(ListView):
    model  = Post
    template_name = 'blog_app/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6
    ordering = ['-created']

    def get_queryset(self):
        queryset = Post.objects.filter(status='published')

        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)

        
        
        return queryset
    

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        print(context['posts'])  # Вывод в консоль для проверки типа объекта
        return context




    
class PostCreateView(LoginRequiredMixin, CreateView):
    '''
    Создние материалров на сайте
    '''
    model= Post
    template_name= 'blog_app/post_create.html'
    form_class = PostCreateForm
    login_url= 'home'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title']='Добавление статьи на сайт'
        return context
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        if not post.slug:  # Если slug отсутствует, генерируем его
            post.slug = slugify(post.title)
        post.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post_list')
    

class PostUpdateView(LoginRequiredMixin, UpdateView):
    '''
    Обновление материалов на сайте
    '''
    model  = Post
    template_name = 'blog_app/post_update.html'
    context_object_name = 'post'
    form_class = PostUpdateForm
    login_url  = 'home'
    success_message = 'Запись была успешно обновлена!'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Обновление статьи '
        return context
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post_list')
    

class PostDetailView(DetailView):
    '''
    Детальный обзор поста
    '''
    model = Post
    template_name = 'blog_app/post_detail.html'
    context_object_name = 'post' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['comments'] = self.object.comments.all()  # Получаем все комментарии к посту
        context['form'] = CommentForm()  # Добавляем пустую форму для комментариев
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()  # Получаем объект поста
        form = CommentForm(request.POST)  # Создаем форму из данных POST-запроса
        if form.is_valid():  # Если форма валидна
            comment = form.save(commit=False)
            comment.post = post  # Связываем комментарий с постом
            comment.user = request.user  # Присваиваем комментарий пользователю
            comment.save()  # Сохраняем комментарий
            return redirect('post_detail', slug=post.slug)  # Перенаправляем на страницу поста
        # Если форма невалидна, возвращаем тот же шаблон с ошибками
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog_app/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']=f'Удаление: {self.object.title}'
        return context
    #добавить чтоб только автор мог удалить пост

class CommentCreateView(CreateView, LoginRequiredMixin):
    model = Comment
    form_class = CommentForm
    template_name = 'blog_app/comment_form.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.user = self.request.user
        form.save()
        return redirect('post_detail', pk=post.pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        return context

    
    