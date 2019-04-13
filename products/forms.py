from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(label = 'Product Name - ', widget = forms.TextInput(attrs = {"placeholder":"Enter product name..."}))
	price = forms.DecimalField(initial = 0.00)
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]
	def clean_price(self,*args,**kwargs):
		price = self.cleaned_data.get("price")
		if price < 0:
			raise forms.ValidationError("You cannot enter a negative value")
		return price
	'''def clean_title(self,*args,**kwargs):
		title = self.cleaned_data.get("title")
		if not "ABC" in title:
			raise forms.ValidationError("Invalid")
		return title
class RawProductForm(forms.Form):
	title = forms.CharField(label = 'Product Name - ', widget = forms.TextInput(attrs = {"placeholder":"Enter product name..."}))
	description = forms.CharField(required = False)
	price = forms.DecimalField()'''