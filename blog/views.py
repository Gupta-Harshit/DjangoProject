from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .forms import ArticleForm
from .models import Article
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

class ArticleDetailView(DetailView):
	template_name = "article_details.html"
	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article,id = id_)

class ArticleCreateView(CreateView):
	template_name = "article_create.html"
	form_class = ArticleForm
	queryset = Article.objects.all()

class ArticleListView(ListView):
	template_name = "article_list.html"
	queryset = Article.objects.all()

class ArticleUpdateView(UpdateView):
	template_name = "article_create.html"
	form_class = ArticleForm
	queryset = Article.objects.all()
	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article,id = id_)

class ArticleDeleteView(DeleteView):
	template_name = "article_delete.html"
	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article,id = id_)
	def get_success_url(self):
		return reverse('blog:article-list')

'''def article_list_view(request):

	queryset = Article.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request,"article_list.html",context)
'''
'''def article_create_view(request):
	form = ArticleForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ArticleForm()
	context = {
		'form': form
	}
	return render(request,"article_create.html",context)'''

'''def article_detail_view(request, id):
	obj = Article.objects.get(id = id)
	context = {
		"object":obj
	}
	return render(request,"article_details.html",context)
'''