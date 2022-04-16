from django.urls import path

from .views import IndexView, AuthorView


urlpatterns = [
    path('author/<str:name>/', AuthorView.as_view(), name='author'),
    path('', IndexView.as_view(), name='index'),
]

