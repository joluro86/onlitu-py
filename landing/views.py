from django.shortcuts import render

from product.models import Producto

def landing_product(request, id):
    if id==1:
        protsan = Producto.objects.get(id=id)
        return render(request, 'landing/protsan.html', {'protsan':protsan})
    
def protsan_formulario_compra(request):

    return render(request, 'landing/protsan_formulario_compra.html')
        
        

   
