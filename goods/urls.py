from django.urls import path,include
from . import views
from .models import HomeDecorDetail, HomeDcor 
import django.contrib.auth.urls



urlpatterns = [
    path('', views.display_index,name='display_index'),
    path('Dcor/', views.display_HomeDcor,name='display_HomeDcor'),
    path('Dcordetail/<str:detail_rank>',views.display_HomeDcorDetail,name='homedcordetail'),
    path('add-to-cart/<int:cart_item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.add_to_cart, name='cart'),
	path('Chart/', views.home_list, name='home_list'),
	path('order/', views.display_order, name='oder'),
	path('error/',views.display_error, name='error'),
    
]




