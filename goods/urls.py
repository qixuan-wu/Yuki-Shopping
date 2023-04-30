from django.urls import path
from . import views
from .models import HomeDecorDetail, HomeDcor 
from account.views import register, login_view


app_name = 'goods'

urlpatterns = [
    path('', views.display_index,name='display_index'),
    path('home/', views.display_home,name='display_home'),
    path('Dcor/', views.display_HomeDcor,name='display_HomeDcor'),
    path('Dcordetail/<str:detail_rank>',views.display_HomeDcorDetail,name='homedcordetail'),
	path('register/', register, name='register'),
	path('login_view/', login_view, name='login_view'),



	# path('shoppingcar',views.add_to_cart,name='add_to_cart')
]




