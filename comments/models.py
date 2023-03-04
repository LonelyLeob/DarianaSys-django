from django.db import models
from darianatoys.settings import AUTH_USER_MODEL
from toys.models import Toy

class Comment(models.Model):
    toy = models.ForeignKey(verbose_name="Игрушка", to=Toy, on_delete=models.CASCADE)
    commenter = models.ForeignKey(verbose_name="Пользователь", to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    positive = models.CharField(verbose_name="Достоинства", max_length=200)
    negative = models.CharField(verbose_name="Недостатки", max_length=200)
    comment = models.CharField(verbose_name="Отзыв", max_length=500)

    def __str__(self) -> str:
        return self.comment if len(self.comment)<20 else self.comment[:20] + "..."

    class Meta:
        verbose_name="Комментарий"
        verbose_name_plural = "Комментарии"