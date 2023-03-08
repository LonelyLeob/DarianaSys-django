from django.db import models
from ckeditor.fields import RichTextField

class Toy(models.Model):
    title = models.CharField(verbose_name="Название", max_length=50, unique=True)
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=10)
    description = RichTextField(verbose_name="Описание")
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name="Игрушка"
        verbose_name_plural = "Игрушки"


def upload_to(instance, filename):
    return f"toys/{instance.toy.pk}/{filename}"

class ToyImage(models.Model):
    title = models.CharField(verbose_name="Название картинки", max_length=255)
    photo = models.ImageField(verbose_name="Фото", upload_to=upload_to)
    toy = models.ForeignKey(verbose_name="Игрушка", to=Toy, on_delete=models.PROTECT, related_name='photos')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name="Картинка"
        verbose_name_plural="Картинки"

class Material(models.Model):
    title = models.TextField(verbose_name="Название материала")
    toy = models.ForeignKey(verbose_name="Игрушка", to=Toy, on_delete=models.PROTECT, related_name='materials')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name="Материал"
        verbose_name_plural = "Материалы"