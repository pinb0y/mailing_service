from django.urls import path

from mail_sender.apps import MailSenderConfig
from mail_sender.views import (
    MailingListView,
    MailingCreateView,
    MailingDeleteView,
    MailingDetailView,
    MailingUpdateView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
    ClientListView,
    MessageCreateView,
    MessageUpdateView,
    MessageListView,
    MessageDeleteView, change_mailing_status,
)

app_name = MailSenderConfig.name

urlpatterns = [
    path("", MailingListView.as_view(), name="mailings"),
    path("mailing/<int:pk>/", MailingDetailView.as_view(), name="detail_mailing"),
    path("create/", MailingCreateView.as_view(), name="create_mailing"),
    path("delete/<int:pk>/", MailingDeleteView.as_view(), name="delete_mailing"),
    path("update/<int:pk>/", MailingUpdateView.as_view(), name="update_mailing"),
    path("create_client/", ClientCreateView.as_view(), name="create_client"),
    path("update_client/<int:pk>/", ClientUpdateView.as_view(), name="update_client"),
    path("delete_client/<int:pk>/", ClientDeleteView.as_view(), name="delete_client"),
    path("clients/", ClientListView.as_view(), name="clients"),
    path("create_message/", MessageCreateView.as_view(), name="create_message"),
    path(
        "update_message/<int:pk>/", MessageUpdateView.as_view(), name="update_message"
    ),
    path(
        "delete_message/<int:pk>/", MessageDeleteView.as_view(), name="delete_message"
    ),
    path("messages/", MessageListView.as_view(), name="messages"),
    path("change_status/<int:pk>/", change_mailing_status, name="change_status"),
]
