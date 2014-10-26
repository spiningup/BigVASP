from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models


class Country(models.Model):
    """
    Country
    """
    name = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=220, null=True, blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return self.code


class State(models.Model):
    """
    STATE
    """
    name = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=220, null=True, blank=True)
    country = models.ForeignKey(Country, blank=True, null=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return self.code


class City(models.Model):
    """
    CITY
    """
    name = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=220, null=True, blank=True)
    state = models.ForeignKey(State, blank=True, null=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return self.name


class User(AbstractUser):
    """
    SystemUser
    """
    photo = models.ImageField(upload_to='profiles', blank=True, null=True)
    date_birth = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=2, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    zip_code = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    mobile_phone = models.CharField(max_length=200, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    work_phone = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=1000, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __unicode__(self):
        return self.username
