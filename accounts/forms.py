from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'department',
            'email',
            'phone',
            'birthday',
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'department',
            'email',
            'phone',
            'birthday',
        )
