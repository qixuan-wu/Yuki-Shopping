from django.core.paginator import Paginator
from .models import HomeDcor,HomeFurnishing,HomeDecorDetail,HomeFurnishingDetail
from django.shortcuts import render, get_object_or_404


def display_index(request):
    return render(request, 'index.html')


def display_home(request):
    return render(request, 'home.html')

def display_HomeDcor(request,):
    homedcor = HomeDcor.objects.all()
    paginator = Paginator(homedcor, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Dcor.html', {'page_obj': page_obj})

def display_HomeDcorDetail(request,name):
    homedcordetail=get_object_or_404(HomeDcor, name=name)
    return render(request, 'templates/Dcor_detail.html', {'homedcordetail':  homedcordetail})









# def display_HomeDcorDetail(request):
# 	home_docr_detail=HomeDcor.objects.all()
# 	goods_id=request.GET.get('name',1)
# 	goods_data=HomeDecorDetail.objects.get(id=goods_id)
#     return render(request, 'Dcor_detail.html', {'home_docr_detail': home_docr_detail})
