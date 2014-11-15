from django import forms
from authsys.models import User
from django.contrib import auth

class signup_form(auth.forms.UserCreationForm):
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


class AuthenticationForm(auth.forms.AuthenticationForm):
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

    def clean(self, *args, **kwargs):
        ''' Override form authentication by checking if the field contains an
        email address instead of a username'''
        user_email = User.objects.filter(email=self.cleaned_data.get('username'))
        if user_email.exists():
            self.cleaned_data['username'] = user_email.first().username

        return super(AuthenticationForm, self).clean(*args, **kwargs)