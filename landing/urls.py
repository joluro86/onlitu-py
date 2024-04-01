from landing.views import landing_product, protsan_formulario_compra

from django.urls import path

urlpatterns = [
    path("<int:id>/", landing_product, name="landing_product"),
    path("realizar_pedido", protsan_formulario_compra, name="formulario_compra_protsan")   
]