from django.urls import path

from mail_sender.apps import MailSenderConfig
from mail_sender.views import MailingListView, MailingCreateView, MailingDeleteView

app_name = MailSenderConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name="mailings"),
    path('create/', MailingCreateView.as_view(), name="create_mailing"),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name="delete_mailing"),
]
