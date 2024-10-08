from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from mail_sender.models import Mailing, Client, Message


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    success_url = reverse_lazy('mail:mailings')
    fields = '__all__'


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = '__all__'

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
    success_url = reverse_lazy('mail:clients')
    fields = '__all__'


class ClientUpdateView(UpdateView):
    model = Client
    success_url = reverse_lazy('mail:clients')
    fields = '__all__'


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("mail:mailings")


class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    success_url = reverse_lazy('mail:messages')
    fields = '__all__'


class MessageUpdateView(UpdateView):
    model = Message
    success_url = reverse_lazy('mail:messages')
    fields = '__all__'


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("mail:mailings")
