from django.shortcuts import render

from product.models import ProductNumberPhone, Producto

def landing_product(request, id):
    if id==1:
        protsan = Producto.objects.get(id=id)
        celular = ProductNumberPhone.objects.get(product=protsan).number
        print(celular)
        return render(request, 'landing/protsan.html', {'protsan':protsan, 'celular':celular})
    
def protsan_formulario_compra(request):

    return render(request, 'landing/protsan_formulario_compra.html')
        
        

   
