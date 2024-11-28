from django.urls import path
from .views import UserLoginView, UserRegisterView, ProfileDetailView, UserLogoutView, ProfileUpdateView

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'), 
    path('profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('profile/<slug:slug>/', ProfileDetailView.as_view(), name='profile_detail'),
    


]
