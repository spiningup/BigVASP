from django import forms
from authsys.models import User
from django.contrib.auth.forms import UserCreationForm


class signin_form(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


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
