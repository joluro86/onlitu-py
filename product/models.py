from django.db import models
from django.urls import reverse
from category.models import Category
from gender.models import Gender

class Producto(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default =0)
    imagen = models.ImageField(upload_to='products/', default=0) 

    class Meta:
        db_table = 'product'
        managed = True
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})


class ProductGender(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_gender'
        managed = True
        verbose_name = 'ProductGender'
        verbose_name_plural = 'ProductGenders'