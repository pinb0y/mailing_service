from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)

from mail_sender.forms import MessageForm, MailingForm, ClientForm
from mail_sender.models import Mailing, Client, Message


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mail:mailings")


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        """Переход к блогу после успешного редактирования"""
        return reverse("mail:detail_mailing", args=[self.kwargs.get("pk")])


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("mail:mailings")


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    success_url = reverse_lazy("mail:clients")
    form_class = ClientForm


class ClientUpdateView(UpdateView):
    model = Client
    success_url = reverse_lazy("mail:clients")
    form_class = ClientForm


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("mail:mailings")


class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mail:messages")


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mail:messages")


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("mail:mailings")
