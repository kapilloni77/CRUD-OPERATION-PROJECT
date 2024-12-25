from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from testapp.models import Product
from django.urls import reverse_lazy
def hello_view(request):
    return render(request,'testapp/Test.html')
class CreateProduct(CreateView):
    model=Product
    fields="__all__"
class ProductList(ListView):
    model=Product
class ProductDetail(DetailView):
    model=Product
class ProductUpdate(UpdateView):
    model=Product
    fields=('pname','price')
class ProductDelete(DeleteView):
    model=Product
    success_url=reverse_lazy('list')
