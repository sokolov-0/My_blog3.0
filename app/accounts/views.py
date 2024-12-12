from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView


from .forms import UserUpdateForm, ProfileUpdateForm, UserRegisterForm, UserLoginForm #нужно создать формы
from .models import Profile#Нужно создать
class ProfileDetailView(DetailView):
    '''
    Класс для детального просмотра профиля
    '''

    model = Profile
    context_object_name='profile'
    template_name = 'accounts/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Профиль пользователя {self.object.user.username}'
        return context
    
class UserRegisterView(CreateView, SuccessMessageMixin):
    '''
    класс регистрации на сайте с формой регистрации

    '''
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')
    success_message = 'Вы успешно зарегистрировались! Можете войти на сайт'
    template_name = 'accounts/user_register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте '
        return context


class UserLoginView(LoginView, SuccessMessageMixin):
    '''
    Класс авторизации на сайте
    '''
    form_class = UserLoginForm
    template_name = 'accounts/user_login.html'
    next_page = 'post_list'
    success_message = 'Добро пожаловать на сайт'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('post_list')



class ProfileUpdateView(UpdateView):
    '''
    Представление для редактирования профиля
    '''
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile_edit.html'

    def get_object(self, queryset = None):
        return self.request.user.profile
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']=f'Редактирование профиля пользователя: {self.request.user.username}'
        
        if self.request.POST:
            context['user_form'] = UserUpdateForm(self.request.POST , instance=self.request.user)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']

        with transaction.atomic():
            # Проверяем, что обе формы валидны
            if form.is_valid() and user_form.is_valid():
                # Сначала сохраняем данные пользователя
                user_form.save()
                # Затем сохраняем профиль
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
        
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('accounts:profile_detail', kwargs={'slug': self.object.slug})
    
    
    


