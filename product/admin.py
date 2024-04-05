from django.contrib import admin
from .models import Producto, ProductGender, ProductNumberPhone

# Las definiciones existentes de ProductoAdmin y ProductNumberPhoneAdmin
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category')
    search_fields = ('name', 'category__name')

class ProductNumberPhoneAdmin(admin.ModelAdmin):
    list_display = ('product', 'number')
    search_fields = ('product__name', 'number')

# Nueva definición para ProductGender
class ProductGenderAdmin(admin.ModelAdmin):
    list_display = ('product', 'gender')  # Mostrar el producto y el género en la lista
    search_fields = ('product__name', 'gender__name')  # Permitir búsqueda por nombre de producto y género

admin.site.register(Producto, ProductoAdmin)
admin.site.register(ProductNumberPhone, ProductNumberPhoneAdmin)
admin.site.register(ProductGender, ProductGenderAdmin)


