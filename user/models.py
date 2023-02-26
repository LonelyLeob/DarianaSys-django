from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = models.CharField(max_length=255, verbose_name='Логин', unique=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя', null=True)
    email = models.CharField(max_length=255, unique=True, verbose_name='Почта')
    telephone = PhoneNumberField(verbose_name="Номер телефона", null=True)
    age = models.IntegerField(verbose_name="Возраст", null=True)
    password = models.CharField(max_length=255, verbose_name='Пароль')

    #off fields
    last_name=None
    date_joined=None

    #constraints
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

class TokenStorage(models.Model):
    user_id = models.ForeignKey(verbose_name="CompareWith", to=User, on_delete=models.CASCADE)
    refresh = models.CharField(verbose_name="Refresh", max_length=255)

    class Meta:
        verbose_name = "TokenObject"
        verbose_name_plural = 'TokenObjects'