from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
	title		=forms.CharField(max_length = 120,widget = forms.TextInput(attrs = {"placeholder":"Enter title..."}))
	writer		=forms.CharField(max_length = 30,widget = forms.TextInput(attrs = {"placeholder":"Enter writer's name..."}))
	description	=forms.CharField(max_length = 200,widget = forms.TextInput(attrs = {"placeholder":"Enter a short description..."}))
	words		=forms.IntegerField()
	class Meta:
		model = Article
		fields = [
			'title',
			'writer',
			'description',
			'words'
		]
	def clean_words(self,*args,**kwargs):
		words = self.cleaned_data.get("words")
		if words < 0:
			raise forms.ValidationError("Value cannot be negative.")
		return words