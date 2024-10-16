from django.urls import reverse_lazy

from pytils.translit import slugify
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)

from blog.forms import BlogForm
from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    extra_context = {"title": "Список постов"}


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    extra_context = {"title": "Создание поста"}
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        """Переопределяем метод, чтобы был корректный слаг"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    extra_context = {"title": "Редактирование блога"}
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        """Переопределяем метод, чтобы был корректный слаг"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {"title": "Пост"}

    def get_object(self, queryset=None):
        """Создаем счетчик просмотров"""
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()

        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    extra_context = {"title": "Удаление поста"}
    success_url = reverse_lazy("blog:blog_list")
