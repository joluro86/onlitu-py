from venta.views import index, guardar_venta, lista_ventas, nosotros, shop, contactanos, shop_by_category, ellas, ellos, ordenar_por_precio

from django.urls import path

urlpatterns = [
    path("", index, name="index"),
    path("nosotros", nosotros, name="nosotros"),
    path("tienda", shop, name="tienda"),
    path("ellas", ellas, name="ellas"),
    path("ellos", ellos, name="ellos"),
    path("contactanos", contactanos, name="contactanos"),
    path("por-categoria/<int:category_id>/", shop_by_category, name="shop_by_category"),
    path("ordenar/", ordenar_por_precio, name="ordenar_por_precio"),
    path("guardar-venta", guardar_venta, name="guardar_venta"),
    path("lista-ventas", lista_ventas, name="lista-ventas"),

]
