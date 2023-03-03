from django.db import models
from ckeditor.fields import RichTextField

class Material(models.Model):
    title = models.TextField(verbose_name="Название материала")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name="Материал"
        verbose_name_plural = "Материалы"

class Toy(models.Model):
    title = models.CharField(verbose_name="Название", max_length=50, unique=True)
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=10)
    description = RichTextField(verbose_name="Описание")
    materials = models.ManyToManyField(verbose_name='Материалы', to=Material)
    photos = models.ManyToManyField(verbose_name="Фото", to="ToyImage", blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name="Игрушка"
        verbose_name_plural = "Игрушки"


def upload_to(instance, filename):
    return f"toys/{instance.title}/{filename}"

class ToyImage(models.Model):
    title = models.CharField(verbose_name="Название картинки", max_length=255)
    photo = models.ImageField(verbose_name="Фото", upload_to=upload_to)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name="Картинка"
        verbose_name_plural="Картинки"
