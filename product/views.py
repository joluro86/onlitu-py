from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto
from .forms import ProductoForm
from django.urls import reverse_lazy

class ProductListView(ListView):
    model = Producto
    context_object_name = 'products'
    template_name = 'products.html'

class ProductDetailView(DetailView):
    model = Producto
    context_object_name = 'product'
    template_name = 'product_detail.html'
    success_url = reverse_lazy('product_list')

class ProductCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Producto
    context_object_name = 'product'
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

