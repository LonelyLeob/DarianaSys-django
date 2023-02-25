from django.db import models

class Material(models.Model):
    title = models.TextField(verbose_name="Название ткани")

class Toy(models.Model):
    title = models.TextField(verbose_name="Название")
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=16)
    description = models.TextField(verbose_name="Описание")
    materials = models.ForeignKey(verbose_name="Материалы", to="Material", on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.title