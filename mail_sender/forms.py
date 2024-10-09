from django.forms import CheckboxInput, ModelForm, ModelMultipleChoiceField, DateInput

from mail_sender.models import Client, Message, Mailing


class StyleFormMixin:
    """Миксин для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class MessageForm(StyleFormMixin, ModelForm):
    """Основная форма создания сообщения рассылки: тема, сообщение, список получателей"""

    recipient = ModelMultipleChoiceField(
        queryset=Client.objects.all(),
    )

    class Meta:
        model = Message
        fields = "__all__"


class MailingForm(StyleFormMixin, ModelForm):
    """Форма для рассылки: время начала, время окончания, периодичность"""

    class Meta:
        model = Mailing
        exclude = ("status",)
        widgets = {
            "start_mailing": DateInput(
                attrs={"type": "date-local", "placeholder": "Введите дату"}
            ),
            "end_mailing": DateInput(
                attrs={"type": "date-local", "placeholder": "Введите дату"}
            ),
        }


class ClientForm(StyleFormMixin, ModelForm):
    """Форма создания клиента"""

    class Meta:
        model = Client
        fields = "__all__"
