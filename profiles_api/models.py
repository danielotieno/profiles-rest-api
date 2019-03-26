from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# User Model


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represent User Profile inside our system """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Use to get users fullname """
        return self.name

    def get_short_name(self):
        """ Use to get users short name """
        return self.name

    def __str__(self):
        """ Django uses this when it converts an object to a string """
        self.email
