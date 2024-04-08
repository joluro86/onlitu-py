from carro.views import ver_carrito, agregar_a_carrito, limpiar_carrito, eliminar_del_carrito
from django.urls import path

urlpatterns = [
    path("", ver_carrito, name="ver-carrito"),
    path("agregar-producto", agregar_a_carrito, name="agregar_a_carrito"),
    path('limpiar/', limpiar_carrito, name='limpiar_carrito'),   
    path('carro/eliminar/<int:product_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
]
