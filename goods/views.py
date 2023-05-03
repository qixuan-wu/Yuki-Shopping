from django.core.paginator import Paginator
from .models import HomeDcor, HomeFurnishing, HomeDecorDetail, HomeFurnishingDetail, cart
from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from decimal import Decimal
from django.conf import settings
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
    paginator = Paginator(homedcor_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Dcor.html', {'page_obj': page_obj})



def display_HomeDcorDetail(request, detail_rank):
    detail = get_object_or_404(HomeDecorDetail, rank=detail_rank)
    sightdetails = HomeDecorDetail.objects.filter(rank=detail_rank)
    return render(request, 'Dcor_detail.html', {'detail': detail, 'sightdetails': sightdetails})


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = float(request.POST['price'].replace(',', '.'))
        quantity = int(request.POST.get('quantity'))
        # 从数据库中查询是否存在该购物车项，如果不存在，则创建一个新的购物车项
        cart_item, created = cart.objects.get_or_create(
            name=name,
            price=price,
            defaults={'quantity': quantity},
        )
        if not created:
            cart_item.quantity=quantity
            cart_item.save()
        cart_list=cart.objects.all()
        total=sum([item.price*item.quantity for item in cart_list])
        return render(request, 'shoppingcar.html',{'cart_list':cart_list, 'new_product':{'name':name,}})
    else:
        cart_list=cart.objects.all()
        total=sum([item.price*item.quantity for item in cart_list])
        return render(request, 'shoppingcar.html',{'cart_list':cart_list, 'total':total})


@login_required
def remove_from_cart(request,cart_item_id):
    cart_item_id = int(cart_item_id)

    cart_list = get_object_or_404(cart, id=cart_item_id)
    cart_list.delete()
    print(cart_item_id)
    return redirect('cart')

