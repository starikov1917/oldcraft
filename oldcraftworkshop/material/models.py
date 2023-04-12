from django.db import models

from product.models import Product
# Create your models here.

class  MaterialType(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Группа материалов")
    slug = models.SlugField(unique=True, verbose_name="Код группы материалов")

    def __str__(self):
        return self.title

class Material(models.Model):
    title = models.CharField(max_length=50, verbose_name="Материал")
    slug = models.SlugField(max_length=20, verbose_name="Код материала")
    availableQuantity = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Доступное количество")
    image = models.ImageField(upload_to="images/materials")
    materialType = models.ForeignKey(MaterialType, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class RequiredMaterialType(models.Model):
    materialType = models.ForeignKey(MaterialType, on_delete=models.PROTECT)
    requiredQuantity = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Необходимое количество")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return "For " + self.product.__str__() + " we need " + str(self.requiredQuantity) + " of " + self.materialType.__str__()


