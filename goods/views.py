from django.core.paginator import Paginator
from .models import HomeDcor,HomeFurnishing,HomeDecorDetail,HomeFurnishingDetail
from django.shortcuts import render

def display_index(request):
    return render(request, 'index.html')


def display_home(request):
    return render(request, 'home.html')

def display_HomeDcor(request):
    home_dcor_list = HomeDcor.objects.all()
    return render(request, 'Dcor.html', {'home_dcor_list': home_dcor_list})

def datapage1(request):
    homedcor = HomeDcor.objects.all()
    paginator = Paginator(my_objects, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Dcor.html', {'page_obj': page_obj})
