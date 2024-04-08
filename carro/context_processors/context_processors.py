def carrito_info(request):
    carrito = request.session.get('carrito', {})
    total_items = sum(item['cantidad'] for item in carrito.values()) if carrito else 0
    return {'total_items_carrito': total_items}
