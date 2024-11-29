from django.urls import path
from .views import UserLoginView, UserRegisterView, ProfileDetailView, UserLogoutView, ProfileUpdateView
from mozilla_django_oidc.views import OIDCAuthenticationRequestView, OIDCLogoutView

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('oidc/login/', OIDCAuthenticationRequestView.as_view(), name='oidc_login'),
    path('oidc/logout/', OIDCLogoutView.as_view(), name='oidc_logout'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('profile/<slug:slug>/', ProfileDetailView.as_view(), name='profile_detail'),
    


]
