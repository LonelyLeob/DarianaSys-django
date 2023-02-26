from django.db import models
from toys.models import Toy

class Purchase(models.Model):
    toy_id = models.ForeignKey(verbose_name="ID игрушки", to=Toy, on_delete=models.PROTECT)
    status_choices = ([
        ("WAIT", "Ожидает исполнения"),
        ("ACCEPT", "Принята"),
        ("END", "Исполнена"),
    ])
    status = models.CharField(verbose_name="Статус", choices=status_choices, max_length=6)

    def __str__(self) -> str:
        return self.toy_id
    
    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"