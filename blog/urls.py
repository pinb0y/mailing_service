from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("create/", BlogCreateView.as_view(), name="add_blog"),
    path("detail/<int:pk>", BlogDetailView.as_view(), name="view_blog"),
    path("update/<int:pk>", BlogUpdateView.as_view(), name="change_blog"),
    path("delete/<int:pk>", BlogDeleteView.as_view(), name="delete_blog"),
]
