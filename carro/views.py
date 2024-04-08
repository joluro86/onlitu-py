from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from product.models import Producto
from venta.models import VentaDetail, Venta, Customer
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_POST

def agregar_a_carrito(request):
    if request.method == 'POST':
        product_id = request.POST.get('producto_id')
        cantidad = request.POST.get('cantidad')
        precio = 0
        
        if int(cantidad)==1:
            precio=79900
        elif int(cantidad)==2:
            precio=134900
        elif int(cantidad)==3:
            precio=159800

        # Verificar si alguno de los valores necesarios es None
        if product_id is None or cantidad is None:
            return HttpResponseBadRequest("Datos incompletos para agregar al carrito.")

        try:
            cantidad = int(cantidad)  # Convertir cantidad a int, manejar si es None o no convertible
        except ValueError:
            # Manejar el caso en que cantidad no sea convertible a int
            return HttpResponseBadRequest("La cantidad proporcionada no es válida.")

        carrito = request.session.get('carrito', {})

        if product_id in carrito:
            carrito[product_id]['cantidad'] += cantidad
            carrito[product_id]['price'] += precio
        else:
            carrito[product_id] = {'cantidad': cantidad, 'price': precio}
        
        request.session['carrito'] = carrito
        print(carrito)

        return redirect('ver-carrito')
    else:
        # Si no es un POST, tal vez quieras redirigir al usuario o mostrar un error
        return redirect('alguna_vista')


def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos_carrito = []
    total = 0

    for product_id, data in carrito.items():
        producto = Producto.objects.get(id=product_id)
        subtotal = data['price']
        total += subtotal
        productos_carrito.append({
            'producto': producto,
            'cantidad': data['cantidad'],
            'price': producto.price,
            'subtotal': subtotal,
            'total': total,
        })
        
    return render(request, 'ver_carrito.html', {'productos_carrito': productos_carrito, 'total': total})

@require_POST
def eliminar_del_carrito(request, product_id):
    carrito = request.session.get('carrito', {})
    product_id_str = str(product_id)
    
    if product_id_str in carrito:
        carrito[product_id_str]
        del carrito[product_id_str]
        request.session['carrito'] = carrito

    return HttpResponseRedirect(reverse('ver-carrito'))

def guardar_venta(request):
    if request.method == 'POST':
        # Obtener datos del cliente como antes...
        
        # Supongamos que recuperas el carrito de la sesión así
        carrito = request.session.get('carrito', {})
        
        if not carrito:
            return render(request, 'error.html', {'mensaje': 'Tu carrito está vacío.'})
        
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        identificacion = request.POST.get('identificacion')
        correo = request.POST.get('correo')
        municipio = request.POST.get('municipio')
        departamento = request.POST.get('departamento')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        
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
        
        # Iterar sobre el carrito para crear los detalles de la venta
        for product_id, data in carrito.items():
            producto = Producto.objects.get(id=product_id)
            VentaDetail.objects.create(
                venta=venta,
                producto=producto,
                quantity=data['cantidad'],
                price=producto.price  # Aquí asumo que tienes un campo 'price' en tu modelo Producto
            )

        # Opcional: limpiar el carrito después de la compra
        del request.session['carrito']

        return render(request, 'landing/compra_exitosa.html')

def limpiar_carrito(request):
    # Asignar un nuevo diccionario vacío al 'carrito' en la sesión
    request.session['carrito'] = {}
    request.session.modified = True  # Asegurar que la sesión se marque como modificada para guardar los cambios
    return redirect('ver-carrito')


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