from carro.views import ver_carrito, agregar_a_carrito
from django.urls import path

urlpatterns = [
    path("", ver_carrito, name="ver-carrito"),
    path("agregar-producto", agregar_a_carrito, name="agregar_a_carrito"),
    
]
