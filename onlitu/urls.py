from django.contrib import admin
from django.urls import include, path
from venta.views import administrador
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ventas/', include('venta.urls')),
    path('categorias/', include('category.urls')),
    path('productos/', include('product.urls')),
    path('generos/', include('gender.urls')),
    path('carro/', include('carro.urls')), 
    path('detalle-producto/', include('landing.urls')),
    path("administrador", administrador, name="administrador"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
