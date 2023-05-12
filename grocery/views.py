from urllib import request
from multiprocessing import context

from django.shortcuts import render

from grocery.models import products
from .forms import Pform
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View

# Create your views here.
def index1(request):
    
 
    product=products.objects.all()

    return render(request,'index.html',{'product':product})

def about(request):
    return render(request,'about.html')
def blogsingle(request):
    return render(request,'blog-single.html')
def blog(request):
    return render(request,'blog.html')
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def contact(request):
    return render(request,'contact.html')
def productsingle(request):
    return render(request,'product-single.html')
def shop(request):
    product=products.objects.all()
    
    return render(request,'shop.html',{'product':product})
def wishlist(request):
    return render(request,'wishlist.html')
def create_view(request):
    context={}
    form=Pform(request.POST,request.FILES)
    if form.is_valid():
        print('valid')
        form.save()
    else:
        print(form.errors)
        print('invalid')

    context['form']=form
    return render(request,"addproduct.html",context)
def update_view(request,id):
    context={}
    obj=get_object_or_404(products,id=id)
    form=Pform(request.POST,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
    context["form"]=form
    return render(request,"updateproduct.html",context)
def delete_view(request,id):
    context={}
    obj=get_object_or_404(products,id=id)
    if request.method=="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request,"deleteproduct.html",context)

def detail_view(request,id):
    context={}
    context["product"]=products.objects.get(id=id)
    return render(request,"product-single.html",context)

