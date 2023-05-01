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



# def add_to_cart(request):
#     if request.method == 'POST':
#         rank = request.POST['rank']
#         name = request.POST['name']
#         price = request.POST['price']
#         quantity = request.POST.get('quantity', 1)
#         cartlist, created = cart.objects.get_or_create(
#             rank=rank,
#             name=name,
#             price=price,
#             quantity=quantity
#         )
#         print(rank, name, price, cartlist)
#         cartlist = cart.objects.all()
#         return render(request, 'shoppingcar.html', {'cartlist': cartlist, 'new_product': {'rank': rank, 'name': name, 'price': price}})

#     else:
#         cartlist = cart.objects.all()
#         return render(request, 'shoppingcar.html', {'cartlist': cartlist, 'new_product': {'rank': rank, 'name': name, 'price': price}})


# def remove_from_cart(request):
#     if request.method == 'POST':
#         rank = request.POST['rank']
#         name = request.POST['name']
#         price = request.POST['price']
#         cart.objects.filter(rank=rank, name=name, price=price).delete()
#         cartlist = cart.objects.all()
#         return render(request, 'shoppingcar.html', {'cartlist': cartlist})


