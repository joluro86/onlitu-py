from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Category

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    
    return render(request, 'category/new_category.html', {'form': form})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'category/categories.html', {'categories':categories})

def edit_category(request, id):
    # Obtén la instancia de la categoría o muestra un error 404 si no existe
    category = get_object_or_404(Category, id=id)
    
    if request.method == 'POST':
        # Pasa la instancia del modelo como argumento 'instance' al formulario
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        # Si no es una solicitud POST, muestra el formulario con los datos existentes
        form = CategoryForm(instance=category)
    
    return render(request, 'category/edit_category.html', {'form': form})

def delete_category(request, id):
    category = get_object_or_404(Category, id=id)   
    category.delete()
    return HttpResponseRedirect(reverse('categories'))
