from django.contrib.auth.mixins import PermissionRequiredMixin
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
    permission_required = "blog.add_blog"
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        """Переопределяем метод, чтобы был корректный слаг"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    extra_context = {"title": "Редактирование блога"}
    permission_required = "blog.change_blog"
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
    permission_required = "blog.view_blog"
    extra_context = {"title": "Пост"}

    def get_object(self, queryset=None):
        """Создаем счетчик просмотров"""
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()

        return self.object


class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    model = Blog
    extra_context = {"title": "Удаление поста"}
    permission_required = "blog.delete_blog"
    success_url = reverse_lazy("blog:blog_list")
