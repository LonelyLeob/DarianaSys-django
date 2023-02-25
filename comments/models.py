from django.db import models

class Comment(models.Model):
    toy_id = models.IntegerField(verbose_name="ID игрушки")
    commenter_id = models.IntegerField(verbose_name="ID пользователя")
    comment = models.CharField(verbose_name="Отзыв", max_length=255)