from django.views.generic import ListView

from .models import Post, Author


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    queryset = Post.objects.all()
    paginate_by = 10
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name_author = Post.objects.get(pk=1).get_author_name()
        # Ищем автора
        author_bd = Author.objects.get(name=name_author)
        context['author'] = author_bd
        return context


class AuthorView(ListView):
    model = Post
    template_name = 'blog/author.html'
    paginate_by = 10
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name_author = Post.objects.get(pk=1).get_author_name()
        # Ищем автора
        author_bd = Author.objects.get(name=name_author)
        context['author'] = author_bd
        return context
