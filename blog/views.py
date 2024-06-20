from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', "slug", "text", "preview", "publication")
    success_url = reverse_lazy('blog:blog_list')


class BlogListView(ListView):
    model = Blog

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', "slug", "text", "preview", "publication")
    success_url = reverse_lazy('blog:blog_list')

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


class BlogDetailView(DetailView):
    model = Blog