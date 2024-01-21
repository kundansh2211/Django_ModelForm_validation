from django import forms
from .models import User
from string import punctuation
from django.core import validators


def password_check(value):
    for v in value:
        if v in punctuation:
            break
    else:
        raise validators.ValidationError("Your password should contain at least one special characters .")


class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=20, validators=[password_check])

    class Meta:
        model = User
        fields = '__all__'

    def clean(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('c_pass')
        if p1 != p2:
            raise validators.ValidationError("Both password Should be Same!!")
