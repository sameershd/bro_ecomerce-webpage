from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name='orders'
 
urlpatterns = [
    path('cart',views.cart,name='cart'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    
    
]