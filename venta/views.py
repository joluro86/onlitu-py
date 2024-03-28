from django.shortcuts import render
from category.models import Category
from gender.models import Gender
from product.models import Producto

applied_filters = {}

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
    return render(request, 'shop.html', {
        'categories': categories,
        'products': products,
        'applied_filters':applied_filters})


def shop_by_category(request, category_id):
    applied_filters={}
    categories = Category.objects.all()
    products = Producto.objects.all()

    # Filtrado por categoría
    products = products.filter(category__id=category_id)
    applied_filters['category'] = categories.get(id=category_id).id

    return render(request, 'shop.html', {
        'categories': categories,
        'products': products,
        'applied_filters':applied_filters})

def ellas(request):
    applied_filters={}
    categories = Category.objects.all()
    products = Producto.objects.all()

    # Filtrado por categoría
    products = products.filter(productgender__gender__id=2)
    applied_filters['gender'] = Gender.objects.get(id=2).id


    return render(request, 'shop.html', {
        'categories': categories,
        'products': products,
        'applied_filters':applied_filters})

def ellos(request):
    categories = Category.objects.all()
    products = Producto.objects.all()
    applied_filters={}
    products = products.filter(productgender__gender__id=1)
    applied_filters['gender'] = Gender.objects.get(id=1).id
    

    return render(request, 'shop.html', {
        'categories': categories,
        'products': products,
        'applied_filters':applied_filters})

def ordenar_por_precio(request, id):
    if id ==0:
        products = Producto.objects.all().order_by('price')
    if id ==1:
        products = Producto.objects.all().order_by('-price')
    if id ==2:
        products = Producto.objects.all().order_by('name')
    print("llegue")
    categories = Category.objects.all()

    return render(request, 'shop.html', {
        'categories': categories,
        'products': products,
        'applied_filters':applied_filters})