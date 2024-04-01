from django.db import models
from django.urls import reverse
from product.models import Producto

class Customer(models.Model):
    name = models.CharField(max_length=100)
    identificacion = models.BigIntegerField(unique=True, null=True, blank=True)  # Asumiendo que quieres que sea opcional y único
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254, null=True, blank=True, unique=True)  # Correo electrónico opcional y único
    address = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)

    class Meta:
        db_table = 'customer'
        managed = True
        verbose_name = 'Cliente'  # Cambiado a español
        verbose_name_plural = 'Clientes'  # Cambiado a español
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Asegúrate de que "customer_detail" sea el nombre correcto de tu vista de detalle de cliente
        return reverse("customer_detail", kwargs={"pk": self.pk})

    

class Venta(models.Model):
    ESTADOS_VENTA = [
        ("F", "Finalizada"),
        ("A", "Anulada"),
    ]
    
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    estate = models.CharField(max_length=1, choices=ESTADOS_VENTA, default="F")

    class Meta:
        db_table = 'venta'
        managed = True
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
    
    def __str__(self):
        return f"Venta {self.id} - {self.estate}"

class VentaDetail(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, verbose_name="Venta relacionada")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto vendido")
    quantity = models.PositiveIntegerField(verbose_name="Cantidad")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")

    class Meta:
        db_table = 'venta_detail'
        managed = True
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Ventas'

    def __str__(self):
        return f"{self.quantity} x {self.producto.name} @ {self.price_per_unit}"


