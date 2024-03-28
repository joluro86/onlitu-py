from django.db import models
from django.urls import reverse
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=100)


    class Meta:
        db_table = 'customer'
        managed = True
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})

