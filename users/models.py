from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    USERNAME_FIELD='email'