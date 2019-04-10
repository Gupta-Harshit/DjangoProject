from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
	my_context = {
		"num": 212,
		"text": "context dictionary (for using databases)",
		"list":[True,12,325,44,'abc'] }
	return render(request,"home.html",my_context)
def about_view(request,*args,**kwargs):
	return render(request,"about.html",{})