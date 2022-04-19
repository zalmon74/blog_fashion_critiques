from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

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


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name_author = Post.objects.get(pk=1).get_author_name()
        # Ищем автора
        author_bd = Author.objects.get(name=name_author)
        context['author'] = author_bd
        next_post = Post.objects.filter(pk__gt=self.get_object().pk).order_by('pk').first()
        context['next_post'] = next_post
        last_post = Post.objects.order_by('last_edit_date').last()
        if last_post != next_post and last_post != self.get_object():
            context['last_post'] = last_post
        return context


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    fields = ['title', 'prew', 'image_prew', 'author', 'content']


class PostEditView(UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    fields = ['title', 'prew', 'image_prew', 'content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_post_pk'] = self.get_object().pk
        context['author'] = self.get_object().author
        return context


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('index')


