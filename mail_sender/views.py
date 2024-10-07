from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from mail_sender.models import Mailing


class MailingListView(ListView):
    model = Mailing

class MailingCreateView(CreateView):
    model = Mailing
    success_url = reverse_lazy("mail:mailings")
    fields = '__all__'

class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("mail:mailings")