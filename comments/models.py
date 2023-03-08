from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from darianatoys.settings import AUTH_USER_MODEL
from toys.models import Toy

class Comment(models.Model):
    toy = models.ForeignKey(verbose_name="Игрушка", to=Toy, on_delete=models.CASCADE, related_name="comments")
    commenter = models.ForeignKey(verbose_name="Пользователь", to=AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(verbose_name="Отзыв", max_length=500)
    mark = models.PositiveSmallIntegerField(verbose_name="Оценка", validators=[MaxValueValidator(5), MinValueValidator(0)])

    def __str__(self) -> str:
        return self.comment if len(self.comment)<20 else self.comment[:20] + "..."

    class Meta:
        verbose_name="Комментарий"
        verbose_name_plural = "Комментарии"