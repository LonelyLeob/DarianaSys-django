from django.db import models
from toys.models import Toy

class Comment(models.Model):
    toy_id = models.ForeignKey(verbose_name="ID игрушки", to=Toy, on_delete=models.PROTECT)
    commenter_id = models.IntegerField(verbose_name="ID пользователя")
    comment = models.CharField(verbose_name="Отзыв", max_length=500)

    def __str__(self) -> str:
        return self.comment if len(self.comment)<20 else self.comment[:20] + "..."

    class Meta:
        verbose_name="Комментарий"
        verbose_name_plural = "Комментарии"