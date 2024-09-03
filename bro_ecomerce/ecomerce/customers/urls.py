from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name='customers'
 
urlpatterns = [
    path('account',views.account,name='account'),
    path('',views.sign_out,name='logout'),
    
    
]