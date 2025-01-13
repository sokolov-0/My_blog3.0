from django.urls import path, reverse_lazy, include
from django.views.generic.base import RedirectView
from .views import UserLoginView, UserRegisterView, ProfileDetailView, UserLogoutView, ProfileUpdateView
from django_keycloak.views import Login, Logout, LoginComplete

app_name = 'accounts'

urlpatterns = [
    # Путь для регистрации пользователя
    #path('register/', UserRegisterView.as_view(), name='user_register'),
    path('login/complete/', LoginComplete.as_view(), name='keycloak_login_complete'),
    path('login/', Login.as_view(), name='user_login'),
    path('logout/', Logout.as_view(), name='logout'),
    
    path('profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),

    # Путь для отображения профиля
    path('profile/<slug:slug>/', ProfileDetailView.as_view(), name='profile_detail'),

]
