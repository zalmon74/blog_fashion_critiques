from django.urls import path

from .views import (IndexView,
                    AuthorView,
                    PostDetailView,
                    PostCreateView,
                    PostEditView,
                    PostDeleteView)


urlpatterns = [
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('author/<str:name>/', AuthorView.as_view(), name='author'),
    path('', IndexView.as_view(), name='index'),
]

