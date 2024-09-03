
from django.urls import path
from . import views

app_name='products'
 
urlpatterns = [
    path('',views.index,name='home'),
    path('list_products/',views.list_products,name='list_products'),
    path('detail_products/<pk>',views.detail_products,name='detail_products')
    
]
