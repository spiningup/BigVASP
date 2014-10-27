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