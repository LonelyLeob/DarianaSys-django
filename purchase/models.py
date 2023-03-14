from django.db import models
from toys.models import Toy
from darianatoys.settings import AUTH_USER_MODEL

class PurchaseItem(models.Model):
    toy = models.ForeignKey(verbose_name="Игрушка", to=Toy, on_delete=models.PROTECT, related_name='toy')
    quantity = models.PositiveIntegerField(verbose_name="Количество")

    def __str__(self):
        return self.toy.__str__()

    class Meta:
        verbose_name = "Предмет заявки"
        verbose_name_plural = "Предметы заявки"

class PurchaseBase(models.Model):
    user = models.ForeignKey(verbose_name='Пользователь', to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="Дата заказа", auto_now_add=True)
    items = models.ManyToManyField(verbose_name="Предметы", to=PurchaseItem)

    def __str__(self) -> str:
        return f"Заявка №{self.pk}"
    
    def get_total(self):
        return [val.toy.price*val.quantity for val in self.items.all()]

    class Meta:
        abstract = True

class Purchase(PurchaseBase):
    status_choices = ([
        ("WAIT", "Ожидает исполнения"),
        ("ACCEPT", "Принята"),
        ("END", "Исполнена"),
    ])
    status = models.CharField(verbose_name="Статус", choices=status_choices, max_length=6, default="WAIT")

    class Meta:
        verbose_name = "Активная заявка"
        verbose_name_plural = "Активные заявки"

class CanceledPurchase(PurchaseBase):
    canceled_at = models.DateTimeField(verbose_name="Дата отмены", auto_now_add=True)

    class Meta:
        verbose_name= "Отмененная заявка"
        verbose_name_plural= "Отмененные заявки"
