from django.urls import path


from index_page.apps import IndexPageConfig
from index_page.views import IndexView

app_name = IndexPageConfig.name

urlpatterns = [path("", IndexView.as_view(), name="index")]
