from django.core.paginator import Paginator
from .models import HomeDcor,HomeFurnishing,HomeDecorDetail,HomeFurnishingDetail
from django.shortcuts import render, get_object_or_404
from urllib.parse import quote, unquote,urlencode


def display_index(request):
    return render(request, 'index.html')

def display_home(request):
    return render(request, 'home.html')
def display_HomeDcor(request):
    homedcor_list = HomeDcor.objects.all()
    paginator = Paginator(homedcor_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Dcor.html', {'page_obj': page_obj})


def display_HomeDcorDetail(request,detail_rank):
    detail=get_object_or_404(HomeDecorDetail,rank=detail_rank)
    sightdetails = HomeDecorDetail.objects.filter(rank=detail_rank)
    return render(request,'Dcor_detail.html', {'detail':detail,'sightdetails':sightdetails})