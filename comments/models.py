from django.db import models

class Comment(models.Model):
    id = models.IntegerField(verbose_name="ID отзыва", primary_key=True)
    toy_id = models.IntegerField(verbose_name="ID игрушки")
    commenter_id = models.IntegerField(verbose_name="ID пользователя")
    comment = models.CharField(verbose_name="Отзыв", max_length=500, )

    def __str__(self) -> str:
        return self.comment if len(self.comment)<20 else self.comment[:20] + "..."

    class Meta:
        verbose_name="Комментарий"
        verbose_name_plural = "Комментарии"