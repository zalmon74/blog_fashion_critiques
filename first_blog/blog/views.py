from django.views.generic import ListView

from .models import Post, Author


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    queryset = Post.objects.all()
    paginate_by = 10
    context_object_name = 'posts'

