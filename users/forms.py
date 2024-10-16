from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordResetForm,
)

from mail_sender.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Форма регистрации пользователя."""

    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserProfileForm(StyleFormMixin, UserChangeForm):
    """Форма редактирования пользователя."""

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone", "avatar", "country")

    def __init__(self, *args, **kwargs):
        """Скрываем поле с паролем."""

        super().__init__(*args, **kwargs)

        self.fields["password"].widget = forms.HiddenInput()


class ResetPasswordForm(StyleFormMixin, PasswordResetForm):
    """Форма для смены пароля."""

    class Meta:
        model = User
        fields = ("email",)
