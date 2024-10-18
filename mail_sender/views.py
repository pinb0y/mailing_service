from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)

from mail_sender.forms import MessageForm, MailingForm, ClientForm
from mail_sender.models import Mailing, Client, Message, MailingTry


class UserLoginRequiredMixin(LoginRequiredMixin):
    """Миксин для добавления адреса страницы логирования."""
    login_url = "/users/"
    permission_denied_message = "Только для авторизованных пользователей"


class MailingListView(UserLoginRequiredMixin, ListView):
    model = Mailing
    permission_required = "mail_sender.view_mailing"
    extra_context = {"title": "Список рассылок"}

    def get_queryset(self, *args, **kwargs):
        """Получаем кверисет со всеми рассылками для суперюзера или менеджера
        и для конкретного пользователя список только его рассылок."""

        user = self.request.user
        queryset = super().get_queryset(*args, **kwargs)

        if user.is_superuser or user.groups.filter(name="manager"):
            return queryset

        return queryset.filter(owner=user)


class MailingDetailView(UserLoginRequiredMixin, DetailView):
    model = Mailing
    permission_required = "mail_sender.view_mailing"

    def get_object(self, queryset=None):
        """Метод разрешающий детально просматривать только свои рассылки."""

        self.object = super().get_object(queryset)

        if (
                self.object.owner == self.request.user
                or self.request.user.is_superuser
                or self.request.user.groups.filter(name="manager")
        ):
            return self.object

        raise Http404("Вы не можете редактировать чужие записи о клиентах")


class MailingCreateView(UserLoginRequiredMixin, CreateView):
    model = Mailing
    permission_required = "mail_sender.add_mailing"
    form_class = MailingForm
    success_url = reverse_lazy("mail:mailings")

    def form_valid(self, form):
        """При создании рассылки привязываем ей владельцем текущего пользователя."""

        form.instance.owner = self.request.user

        return super().form_valid(form)


class MailingUpdateView(UserLoginRequiredMixin, UpdateView):
    model = Mailing
    permission_required = "mail_sender.change_mailing"
    form_class = MailingForm

    def get_object(self, queryset=None):
        """Метод разрешающий редактировать только свои рассылки."""

        self.object = super().get_object(queryset)

        if self.object.owner == self.request.user or self.request.user.is_superuser:
            return self.object

        raise Http404("Вы не можете редактировать чужие записи о клиентах")

    def get_success_url(self):
        """Переход к блогу после успешного редактирования"""
        return reverse("mail:detail_mailing", args=[self.kwargs.get("pk")])


class MailingDeleteView(UserLoginRequiredMixin, DeleteView):
    model = Mailing
    permission_required = "mail_sender.delete_mailing"
    success_url = reverse_lazy("mail:mailings")

    def get_object(self, queryset=None):
        """Метод разрешающий удалять только свои рассылки."""

        self.object = super().get_object(queryset)

        if self.object.owner == self.request.user or self.request.user.is_superuser:
            return self.object

        raise Http404("Вы не можете редактировать чужие записи о клиентах")


class ClientListView(UserLoginRequiredMixin, ListView):
    model = Client
    permission_required = "mail_sender.view_client"

    def get_queryset(self, *args, **kwargs):
        """Получаем кверисет со всеми клиентами для суперюзера или менеджера
                и для конкретного пользователя список только его клиентов."""

        user = self.request.user
        queryset = super().get_queryset(*args, **kwargs)

        if user.is_superuser or user.groups.filter(name="manager"):
            return queryset

        return queryset.filter(owner=user)


class ClientCreateView(UserLoginRequiredMixin, CreateView):
    model = Client
    success_url = reverse_lazy("mail:clients")
    form_class = ClientForm
    permission_required = "mail_sender.add_client"

    def form_valid(self, form):
        """Метод привязывает текущего пользователя к клиенту при создании."""

        form.instance.owner = self.request.user

        return super().form_valid(form)


class ClientUpdateView(UserLoginRequiredMixin, UpdateView):
    model = Client
    success_url = reverse_lazy("mail:clients")
    form_class = ClientForm
    permission_required = "mail_sender.change_client"

    def get_object(self, queryset=None):
        """Метод разрешающий редактировать только своих клиентов."""

        self.object = super().get_object(queryset)

        if self.object.owner == self.request.user or self.request.user.is_superuser:
            return self.object

        raise Http404("Вы не можете редактировать чужие записи о клиентах")


class ClientDeleteView(UserLoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("mail:mailings")
    permission_required = "mail_sender.delete_client"

    def get_object(self, queryset=None):
        """Метод разрешающий удалять только своих клиентов."""
        self.object = super().get_object(queryset)

        if self.object.owner == self.request.user or self.request.user.is_superuser:
            return self.object

        raise Http404("Вы не можете редактировать чужие записи о клиентах")


class MessageListView(UserLoginRequiredMixin, ListView):
    model = Message
    permission_required = "mail_sender.view_message"

    def get_queryset(self, *args, **kwargs):
        """Получаем кверисет со всеми сообщениями для суперюзера или менеджера
                и для конкретного пользователя список только его сообщений."""

        user = self.request.user
        queryset = super().get_queryset(*args, **kwargs)

        if user.is_superuser or user.groups.filter(name="manager"):
            return queryset

        return queryset.filter(owner=user)


class MessageCreateView(UserLoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mail:messages")
    permission_required = "mail_sender.add_message"

    def form_valid(self, form):
        """Метод привязывает текущего пользователя к сообщению."""

        form.instance.owner = self.request.user

        return super().form_valid(form)


class MessageUpdateView(UserLoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mail:messages")
    permission_required = "mail_sender.change_message"

    def get_object(self, queryset=None):
        """Метод разрешающий редактировать только свои сообщения."""

        self.object = super().get_object(queryset)

        if self.object.owner == self.request.user or self.request.user.is_superuser:
            return self.object

        raise Http404("Вы не можете редактировать чужие записи о клиентах")


class MessageDeleteView(UserLoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy("mail:mailings")
    permission_required = "mail_sender.delete_message"

    def get_object(self, queryset=None):
        """Метод разрешающий удалять только свои сообщения."""

        self.object = super().get_object(queryset)

        if self.object.owner == self.request.user or self.request.user.is_superuser:
            return self.object

        raise Http404("Вы не можете редактировать чужие записи о клиентах")


def change_mailing_status(requests, pk):
    """ Вьюха для смены статуса рассылки менеджером"""

    mailing = Mailing.objects.get(pk=pk)

    if mailing.status == "Приостановлена":
        mailing.status = "Запущена"
    else:
        mailing.status = "Приостановлена"

    mailing.save()

    return redirect(reverse("mail:mailings"))

class MailingTryListView(LoginRequiredMixin, ListView):
    model = MailingTry
