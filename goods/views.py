from django.core.paginator import Paginator
from .models import HomeDcor, HomeFurnishing, HomeDecorDetail, HomeFurnishingDetail
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

def display_index(request):
    return render(request, 'index.html')

def display_home(request):
    return render(request, 'home.html')


def display_HomeDcor(request):
    query = request.GET.get('query')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    homedcor_list = HomeDcor.objects.all()
    if query:
        homedcor_list = homedcor_list.filter(Q(rank__icontains=query) | Q(name__icontains=query))
    if min_price:
        homedcor_list = homedcor_list.filter(price__gte=min_price)
    if max_price:
        homedcor_list = homedcor_list.filter(price__lte=max_price)
    paginator = Paginator(homedcor_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Dcor.html', {'page_obj': page_obj})



def display_HomeDcorDetail(request, detail_rank):
    detail = get_object_or_404(HomeDecorDetail, rank=detail_rank)
    sightdetails = HomeDecorDetail.objects.filter(rank=detail_rank)
    return render(request, 'Dcor_detail.html', {'detail': detail, 'sightdetails': sightdetails})



