from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import (
    BlogListView,
    BlogCreateView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("create/", BlogCreateView.as_view(), name="add_blog"),
    path(
        "view/<str:slug>/", cache_page(60)(BlogDetailView.as_view()), name="view_blog"
    ),
    path("update/<str:slug>/", BlogUpdateView.as_view(), name="change_blog"),
    path("delete/<str:slug>/", BlogDeleteView.as_view(), name="delete_blog"),
]
