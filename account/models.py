from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# https://www.youtube.com/watch?v=eCeRC7E8Z7Y


class AccountManager(BaseUserManager):
    pass


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=25, unique=True)
    display_name = models.CharField(max_length=25, unique=True)
    homepage = models.URLField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    date_joined = models.DateTimeField(
        verbose_name='date-joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last-login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'age', 'display_name']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
