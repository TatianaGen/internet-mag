from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):  # UserCreationForm - форма для регистрации
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')