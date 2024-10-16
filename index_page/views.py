from random import sample

from django.views.generic import TemplateView

from blog.services import get_posts_from_cache
from index_page.services import get_mailings_from_cache, get_clients_from_cache


class IndexView(TemplateView):
    template_name = "index_page/index.html"

    def get_context_data(self, **kwargs):
        """
        Добавляем в контекст данные по активным пользователям, рассылкам и 3 случайных поста из блога.
        """
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Главная"
        mailings = get_mailings_from_cache()
        context_data["count_mailing"] = mailings.count()
        active_mailings_count = mailings.filter(status="Запущена").count()
        context_data["active_mailings_count"] = active_mailings_count
        clients_from_cache = get_clients_from_cache()
        unique_clients_count = clients_from_cache.distinct().count()
        context_data["unique_clients_count"] = unique_clients_count
        posts_from_cache = get_posts_from_cache()
        posts = list(posts_from_cache.filter(is_published=True))
        context_data["random_blog_posts"] = sample(posts, min(3, len(posts)))

        return context_data
