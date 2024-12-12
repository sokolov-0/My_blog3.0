from django.urls import path, reverse_lazy, include
from django.views.generic.base import RedirectView
from .views import UserLoginView, UserRegisterView, ProfileDetailView, UserLogoutView, ProfileUpdateView
from mozilla_django_oidc.views import OIDCAuthenticationRequestView, OIDCLogoutView, OIDCAuthenticationCallbackView

app_name = 'accounts'

urlpatterns = [
    # Путь для регистрации пользователя
    path('register/', UserRegisterView.as_view(), name='user_register'),
    


    # OIDC маршруты для аутентификации
    path('oidc/login/', OIDCAuthenticationRequestView.as_view(), name='oidc_login'),
    path('oidc/logout/', OIDCLogoutView.as_view(), name='oidc_logout'),
    path('oidc/', include('mozilla_django_oidc.urls')),#, namespace='oidc'
    path('oidc/callback/', OIDCAuthenticationCallbackView.as_view(), name='oidc_callback'),

    # Путь для редактирования профиля
    path('profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),

    # Путь для отображения профиля
    path('profile/<slug:slug>/', ProfileDetailView.as_view(), name='profile_detail'),

    # Путь для логина через редирект на OIDC
    path('login/', RedirectView.as_view(url=reverse_lazy('oidc_login')), name='user_login'),
]
