from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDetailView, PostDeleteView,CommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create/', PostCreateView.as_view(), name='post_create' ),
    path('update/<slug:slug>/', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path('delete/<slug:slug>/', PostDeleteView.as_view(), name='post_delete' ),
]
