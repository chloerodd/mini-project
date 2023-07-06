from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Shoe
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import redirect
from django.views import View 
from .models import Shoe, Store, ShoppingCart
# Create your views here.


class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shoppingcart"] = ShoppingCart.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"
    
class ShoeList(TemplateView):
    template_name="shoe_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["shoes"] = Shoe.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["shoes"] = Shoe.objects.all()
            context["header"] = "Shoes in My Closet"
        return context
        
    
class Shoes:
    def __init__(self, name, image, price):
        self.name = name
        self.image = image 
        self.price = price
        
shoes = [
    Shoes("Panda Dunk Low", "https://ibb.co/1GJMfwS", "$145"),
    Shoes("New Balance 550 Vintage Teal", "https://ibb.co/KhMLcG1", "$110"),
]

class ShoeCreate(CreateView):
    model = Shoe
    fields = ['name', 'img', 'price', 'verified_shoe']
    template_name = "shoe_create.html"
    def get_success_url(self):
        return reverse('shoe_detail', kwargs={'pk':self.object.pk})
    
    
class ShoeDetail(DetailView):
    model = Shoe
    template_name = "shoe_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shoppingcart"] = ShoppingCart.objects.all()
        return context
    
    
class ShoeUpdate(UpdateView):
    model = Shoe
    fields = ['name', 'img', 'price', 'verified_shoe']
    template_name = "shoe_update.html"
    def get_success_url(self):
        return reverse('shoe_detail', kwargs={'pk':self.object.pk})
    
    
class ShoeDelete(DeleteView):
    model = Shoe
    template_name = "shoe_delete_confirmation.html"
    success_url = "/shoes/"
    
    
class StoreCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        shoe = Shoe.objects.get(pk=pk)
        Store.objects.create(title=title, artist=artist)
        return redirect('shoe_detail', pk=pk)
    
    
class ShoppingCartStoreAssoc(View):
    
    def get(self, request, pk, store_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            ShoppingCart.objects.get(pk=pk).stores.remove(store_pk)
        if assoc == "add":
            ShoppingCart.objects.get(pk=pk).stores.add(store_pk)
        return redirect('home')