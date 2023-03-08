from django.db import models
from toys.models import Toy
from darianatoys.settings import AUTH_USER_MODEL

class Purchase(models.Model):
    user = models.ForeignKey(verbose_name='Пользователь', to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_choices = ([
        ("WAIT", "Ожидает исполнения"),
        ("ACCEPT", "Принята"),
        ("END", "Исполнена"),
    ])
    created_at = models.DateTimeField(verbose_name="Дата заказа", auto_now_add=True)
    status = models.CharField(verbose_name="Статус", choices=status_choices, max_length=6, default="WAIT")

    def __str__(self) -> str:
        return f"Заявка №{self.pk}"
    
    @property
    def items(self):
        return self.items_set.all()

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def get_total(self):
        return [val.toy.price*val.quantity for val in self.items.all()]
    
class PurchaseItem(models.Model):
    toy = models.ForeignKey(verbose_name="Игрушка", to=Toy, on_delete=models.PROTECT, related_name='toy')
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    purchase = models.ForeignKey(verbose_name="Заявка", to=Purchase, on_delete=models.PROTECT, related_name='items')

    def __str__(self):
        return self.toy.__str__()

    class Meta:
        verbose_name = "Предмет заявки"
        verbose_name_plural = "Предметы заявки"