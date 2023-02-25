from django.db import models

class Material(models.Model):
    id = models.IntegerField(verbose_name="ID материала", primary_key=True)
    title = models.TextField(verbose_name="Название материала")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name="Материал"
        verbose_name_plural = "Материалы"

class Toy(models.Model):
    id = models.IntegerField(verbose_name="ID игрушки", primary_key=True)
    title = models.CharField(verbose_name="Название", max_length=50, unique=True)
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=10)
    description = models.CharField(verbose_name="Описание", max_length=500)
    materials = models.ForeignKey(verbose_name="Материалы", to="Material", on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name="Игрушка"
        verbose_name_plural = "Игрушки"