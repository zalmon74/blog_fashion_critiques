from django.urls import path

from .views import IndexView, AuthorView, PostDetailView


urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('author/<str:name>/', AuthorView.as_view(), name='author'),
    path('', IndexView.as_view(), name='index'),
]

