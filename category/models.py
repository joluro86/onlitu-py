from django.db import models
from django.urls import reverse

class Category(models.Model):
    name= models.CharField(max_length=100)    

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
