from django.shortcuts import render, redirect
from category.models import Category
from gender.models import Gender
from product.models import Producto
import json
from .models import Customer, Producto, Venta, VentaDetail

applied_filters = {}

applied_filters_menu = {}

def index(request):
    return render(request, 'index.html')

def administrador(request):
    return render(request, 'administrador.html')

def nosotros(request):
    return render(request, 'about.html')

def contactanos(request):
    return render(request, 'contact.html')

def shop(request):
    categories = Category.objects.all()
    products = Producto.objects.all().order_by('price')
    applied_filters={}
    applied_filters_menu = {}
    return render(request, 'shop.html', {
        'categories': categories,
        'products': products,
        'applied_filters':applied_filters,
        'applied_filters_menu' : applied_filters_menu})


def shop_by_category(request, category_id):
    categories = Category.objects.all()
    products = Producto.objects.all()
    applied_filters={}
    applied_filters_menu = {}
    # Filtrado por categoría
    products = products.filter(category__id=category_id)
    applied_filters['category'] = categories.get(id=category_id).id
    applied_filters_menu['category'] = categories.get(id=category_id)
    return render(request, 'shop.html', {
        'categories': categories,
        'products': products,
        'applied_filters':applied_filters,
        'applied_filters_menu' : applied_filters_menu})

def ellas(request):
    categories = Category.objects.all()
    products = Producto.objects.all()
    applied_filters={}
    applied_filters_menu = {}
    # Filtrado por categoría
    products = products.filter(productgender__gender__id=2)
    applied_filters['gender'] = Gender.objects.get(id=2).id
    applied_filters_menu['gender'] = Gender.objects.get(id=2)

    return render(request, 'shop.html', {
        'categories': categories,
        'products': products,
        'applied_filters':applied_filters,
        'applied_filters_menu' : applied_filters_menu})

def ellos(request):
    categories = Category.objects.all()
    products = Producto.objects.all()
    products = products.filter(productgender__gender__id=1)
    applied_filters={}
    applied_filters_menu = {}
    applied_filters['gender'] = Gender.objects.get(id=1).id
    applied_filters_menu['gender'] = Gender.objects.get(id=1)

    return render(request, 'shop.html', {
        'categories': categories,
        'products': products,
        'applied_filters':applied_filters,
        'applied_filters_menu' : applied_filters_menu})

def ordenar_por_precio(request):

    products = Producto.objects.all()

    criterio_ordenacion = request.GET.get('ordenar_por', '')

    # Asumiendo que applied_filter viene como una cadena representando un diccionario, por ejemplo, "{'gender': 2}"
    applied_filter_str = request.GET.get('applied_filter', '{}')  # '{}' como valor por defecto para representar un diccionario vacío
    try:
        # Asegúrate de que la cadena esté formateada correctamente para JSON
        if applied_filter_str:
            applied_filter_str = applied_filter_str.replace("'", "\"")
        applied_filter = json.loads(applied_filter_str)
    except json.JSONDecodeError:
        applied_filter = {}

    if 'gender' in applied_filter or 'category' in applied_filter:
        if criterio_ordenacion == 'precio_mas_bajo' and 'gender' in applied_filter:
            products = Producto.objects.filter(productgender__gender__id=applied_filter['gender']).order_by('price')
            applied_filters_menu={}
            applied_filters={}
            applied_filters['gender'] = Gender.objects.get(id=applied_filter['gender']).id
            applied_filters_menu['gender'] = Gender.objects.get(id=applied_filter['gender'])
            applied_filters_menu['price'] = 'Precio mas bajo'
        
        if criterio_ordenacion == 'precio_mas_alto' and 'gender' in applied_filter:
            products = Producto.objects.filter(productgender__gender__id=applied_filter['gender']).order_by('-price')
            applied_filters_menu={}
            applied_filters={}
            applied_filters['gender'] = Gender.objects.get(id=applied_filter['gender']).id
            applied_filters_menu['gender'] = Gender.objects.get(id=applied_filter['gender'])
            applied_filters_menu['price'] = 'Precio mas alto'
        
        if criterio_ordenacion == 'orden_alfabetico' and 'gender' in applied_filter:
            products = Producto.objects.filter(productgender__gender__id=applied_filter['gender']).order_by('name')
            applied_filters_menu={}
            applied_filters={}
            applied_filters['gender'] = Gender.objects.get(id=applied_filter['gender']).id
            applied_filters_menu['gender'] = Gender.objects.get(id=applied_filter['gender'])
            applied_filters_menu['price'] = 'Orden alfabetico'

        if criterio_ordenacion == 'precio_mas_bajo' and 'category' in applied_filter:
            products = Producto.objects.filter(category__id=applied_filter['category']).order_by('price')
            applied_filters_menu={}
            applied_filters={}
            applied_filters['category'] = Category.objects.get(id=applied_filter['category']).id
            applied_filters_menu['category'] = Category.objects.get(id=applied_filter['category'])
            applied_filters_menu['price'] = 'Precio mas bajo'
            print(applied_filters)
            print(applied_filters_menu)
        
        if criterio_ordenacion == 'precio_mas_alto' and 'category' in applied_filter:
            products = Producto.objects.filter(category__id=applied_filter['category']).order_by('-price')
            applied_filters_menu={}
            applied_filters={}
            applied_filters['category'] = Category.objects.get(id=applied_filter['category']).id
            applied_filters_menu['category'] = Category.objects.get(id=applied_filter['category'])
            applied_filters_menu['price'] = 'Precio mas alto'
            print(applied_filters)
            print(applied_filters_menu)

        if criterio_ordenacion == 'orden_alfabetico' and 'category' in applied_filter:
            products = Producto.objects.filter(category__id=applied_filter['category']).order_by('name')
            applied_filters_menu={}
            applied_filters={}
            applied_filters['category'] = Category.objects.get(id=applied_filter['category']).id
            applied_filters_menu['category'] = Category.objects.get(id=applied_filter['category'])
            applied_filters_menu['price'] = 'Orden alfabetico'

    else:
        applied_filters_menu={}
        applied_filters={}
        if criterio_ordenacion == 'precio_mas_bajo':
            products = Producto.objects.all().order_by('price')
            applied_filters_menu['price'] = 'Precio mas bajo'

        if criterio_ordenacion == 'precio_mas_alto':
            products = Producto.objects.all().order_by('-price')
            applied_filters_menu['price'] = 'Precio mas alto'

        if criterio_ordenacion == 'orden_alfabetico':
            products = Producto.objects.all().order_by('name')
            applied_filters_menu['price'] = 'Orden alfabetico'

    
    categories = Category.objects.all()
    
    return render(request, 'shop.html', {
        'categories': categories,
        'products': products,
        'applied_filters':applied_filters,
        'applied_filters_menu' : applied_filters_menu})


def guardar_venta(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        identificacion = request.POST.get('identificacion')
        correo = request.POST.get('correo')
        municipio = request.POST.get('municipio')
        departamento = request.POST.get('departamento')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        cantidad = request.POST.get('cantidad')
        
        # Crear o actualizar el cliente
        customer, created = Customer.objects.update_or_create(
            identificacion=identificacion,
            defaults={'name': nombre, 'email': correo, 'phone': telefono, 'address': direccion, 'municipio': municipio, 'departamento': departamento}
        )
        
        # Crear la venta
        venta = Venta.objects.create(
            customer=customer,
            estate='F'  # Estado 'Finalizada', asumiendo que esto es lo que deseas
        )
        
        # Crear detalle de la venta (asumiendo un único producto por simplificación)
        producto = Producto.objects.first()  # Aquí deberías tener una lógica para seleccionar el producto correcto, por ahora solo tomo el primero como ejemplo
        VentaDetail.objects.create(
            venta=venta,
            producto=producto,
            quantity=int(cantidad),  # 'cantidad' es un string como '79900', '134900', '159800', así que tomamos el primer carácter para la cantidad
            price= float(cantidad[0])  # Calcular el precio por unidad basado en el valor seleccionado
        )
        
        return render(request, 'landing/compra_exitosa.html')  # Redirigir a una página de confirmación, por ejemplo
    
    else:
        # Si no es una solicitud POST, simplemente muestra el formulario
        return render(request, 'protsan_formulario_compra.html')
    
def lista_ventas(request):
    # Recupera todas las instancias de Venta de la base de datos
    ventas = Venta.objects.all().order_by('-date')  # Ordenadas por fecha, de la más reciente a la más antigua

    # Pasa las ventas al template
    context = {'ventas': ventas}
    return render(request, 'ventas_list.html', context)


