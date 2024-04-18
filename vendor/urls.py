
#kda ana 3amalt import l kol l ana 3yzah 

from django.urls import path
from . import views



urlpatterns = [

path('index', views.index, name='index'),
path('vendordashboard', views.vendordashboard, name='vendordashboard'),
path('vendorlogin', views.vendorlogin, name='vendorlogin'),
path('vendorsignup', views.vendorsignup, name='vendorsignup'),
path('productmanagment', views.productmanagment, name='productmanagment'),
path('vendoruserprofile', views.vendoruserprofile, name='vendoruserprofile'),
path('signup/', views.signup, name='signup'),
path('reports', views.reports, name='reports'),
path('products/', views.products_view, name='products'),
path('add_product', views.add_product, name='add_product'),
path('sales', views.sales, name='sales'),


#path('reem', views.index, name='index') da ka2eny ba2ool www.123.com/vendors/reem


]