from django.shortcuts import render, redirect, get_object_or_404
from .forms import GenderForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Gender

def add_gender(request):
    if request.method == 'POST':
        form = GenderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genders')
    else:
        form = GenderForm()
    
    return render(request, 'new_gender.html', {'form': form})

def genders(request):
    genders = Gender.objects.all()
    return render(request, 'genders.html', {'genders':genders})

def edit_gender(request, id):
    # Obtén la instancia de la categoría o muestra un error 404 si no existe
    gender = get_object_or_404(Gender, id=id)
    
    if request.method == 'POST':
        # Pasa la instancia del modelo como argumento 'instance' al formulario
        form = GenderForm(request.POST, instance=gender)
        if form.is_valid():
            form.save()
            return redirect('genders')
    else:
        # Si no es una solicitud POST, muestra el formulario con los datos existentes
        form = GenderForm(instance=gender)
    
    return render(request, 'edit_gender.html', {'form': form})

def delete_gender(request, id):
    category = get_object_or_404(Gender, id=id)   
    category.delete()
    return HttpResponseRedirect(reverse('genders'))

