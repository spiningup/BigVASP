# Django Modules
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

# App Modules
from authsys.models import User
from authsys.forms import signin_form


def index(request):
    if request.user.is_authenticated():
        return redirect(reverse('list'))
    else:
        return redirect(reverse('signin'))


def signin(request):
    """
    SignIn View
    """
    if request.user.is_authenticated():
        return redirect(reverse('list'))
    else:
        if request.method == 'POST':
            form = signin_form(request.POST or None)
            if form.is_valid():
                email = request.POST.get('email', '')
                password = request.POST.get('password', '')
                try:
                    user = User.objects.get(email=email)
                except:
                    return redirect(reverse('signin'))
                if user.is_active:
                    user_auth = authenticate(username=email, password=password)
                    if user_auth is not None:
                        login(request, user_auth)
                        return redirect(reverse('list'))
                    else:
                        return redirect(reverse('signin'))
            else:
                return redirect(reverse('signin'))
        else:
            ctx = {}
            ctx['form'] = signin_form()
            return render(request, 'authsys/signin.html', ctx)


def signout(request):
    """
    SignOut View
    """
    logout(request)
    return redirect(reverse('signin'))
