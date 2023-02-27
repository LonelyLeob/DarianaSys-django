from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = models.CharField(verbose_name='Логин', max_length=255, unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255, null=True)
    email = models.CharField(verbose_name='Почта', max_length=255, unique=True)
    telephone = PhoneNumberField(verbose_name="Номер телефона", null=True)
    age = models.IntegerField(verbose_name="Возраст", null=True)
    password = models.CharField(verbose_name='Пароль', max_length=255)

    #off fields
    last_name=None
    date_joined=None
    last_login=None

    #constraints
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

class TokenStorage(models.Model):
    user_id = models.ForeignKey(verbose_name="CompareWith", to=User, on_delete=models.CASCADE)
    refresh = models.CharField(verbose_name="Refresh", max_length=255)

    class Meta:
        verbose_name = "TokenObject"
        verbose_name_plural = 'TokenObjects'