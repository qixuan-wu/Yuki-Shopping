from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_index,name='display_index'),
	path('home/', views.display_home,name='display_home'),
]