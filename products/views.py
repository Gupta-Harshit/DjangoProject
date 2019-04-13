from django.shortcuts import render
from .models import Product
from .forms import ProductForm
'''def product_create_view(request):
	my_form = RawProductForm()
	if request.method == "POST":
		my_form = RawProductForm(request.POST)
		if my_form.is_valid():
			Product.objects.create(**my_form.cleaned_data) #roughly same as form.save()
	context = {
		"form":my_form
	}
	return render(request,"products/product_create.html",context)'''
# Create your views here.
def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context = {
		'form': form
	}
	return render(request,"products/product_create.html",context)

def product_detail_view(request,id):
	obj = Product.objects.get(id = id)
	context = {
		"object": obj
	}
	return render(request,"products/product_details.html",context)

def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request,"products/product_list.html",context)