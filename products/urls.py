from django.urls import path
from .views import *

app_name = 'products'
urlpatterns = [
	path('', product_list_view, name = 'product-list'),
	path('create/', product_create_view, name = 'product-create'),
	path('<int:id>/', product_detail_view, name = 'product-detail')
]