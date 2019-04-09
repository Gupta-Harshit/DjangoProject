from django.db import models
from django.urls import reverse
# Create your models here.
class Article(models.Model):
	title		=models.CharField(max_length = 120)
	writer		=models.CharField(max_length = 30)
	description	=models.TextField(max_length = 200,null = True,blank = True)
	words		=models.IntegerField()
	def get_absolute_url(self):
		return reverse("blog:article-detail",kwargs={"id":self.id})