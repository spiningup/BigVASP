from django import forms
from authsys.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class signup_form(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class AuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
                u'maxlength': '100',
                u'class': 'form-control',
                u'type': 'username',
                u'placeholder': 'Username',
                u'required': '',
                u'autofocus': ''
            })

        self.fields['password'].widget.attrs.update({
                u'max_length': '32',
                u'class': 'form-control',
                u'type': 'password',
                u'placeholder': 'Password',
                u'required':''
            })