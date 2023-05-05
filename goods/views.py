from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import HomeDcor, HomeDecorDetail, cart
from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from decimal import Decimal
from django.conf import settings
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages

def display_index(request):
    return render(request, 'index.html')


def display_HomeDcor(request):
    query = request.GET.get('query')
    homedcor_list = HomeDcor.objects.all()
    if query:
        homedcor_list = homedcor_list.filter(Q(rank__icontains=query) | Q(name__icontains=query))
    paginator = Paginator(homedcor_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Dcor.html', {'page_obj': page_obj})
    if not page_obj:
        messages.warning(request, 'No results found.')
    return render(request, 'Dcor.html', {'page_obj': page_obj})


def display_HomeDcorDetail(request, detail_rank):
    detail = get_object_or_404(HomeDecorDetail, rank=detail_rank)
    sightdetails = HomeDecorDetail.objects.filter(rank=detail_rank)
    return render(request, 'Dcor_detail.html', {'detail': detail, 'sightdetails': sightdetails})

# @login_required
# def add_to_cart(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         price = float(request.POST['price'].replace(',', '.'))
#         quantity = int(request.POST.get('quantity'))
#         # 从数据库中查询是否存在该购物车项，如果不存在，则创建一个新的购物车项
#         cart_item, created = cart.objects.get_or_create(
#             name=name,
#             price=price,
#             defaults={'quantity': quantity},
#         )
#         if not created:
#             cart_item.quantity=quantity
#             cart_item.save()
#         cart_list=cart.objects.all()
#         total=sum([item.price*item.quantity for item in cart_list])
#         return render(request, 'shoppingcar.html',{'cart_list':cart_list, 'new_product':{'name':name,}})
#     else:
#         cart_list=cart.objects.all()
#         total=sum([item.price * item.quantity for item in cart_list])
#         return render(request, 'shoppingcar.html',{'cart_list':cart_list, 'total':total})

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            price = float(request.POST['price'].replace(',', '.'))
            quantity = int(request.POST.get('quantity'))
           
            cart_item, created = cart.objects.get_or_create(
                name=name,
                price=price,
                defaults={'quantity': quantity},
            )
            if not created:
                cart_item.quantity=quantity
                cart_item.save()
        except:
            # Handling exceptions and displaying error messages to the user
            error_message = "Failed to add item to cart. Please try again later."
            return render(request, 'shoppingcar.html', {'error_message': error_message})
        
        cart_list=cart.objects.all()
        total=sum([item.price*item.quantity for item in cart_list])
        return render(request, 'shoppingcar.html', {'cart_list': cart_list, 'new_product': {'name': name}})
    else:
        cart_list=cart.objects.all()
        total=sum([item.price * item.quantity for item in cart_list])
        return render(request, 'shoppingcar.html', {'cart_list': cart_list, 'total': total})


# @login_required
# def remove_from_cart(request,cart_item_id):
#     cart_item_id = int(cart_item_id)

#     cart_list = get_object_or_404(cart, id=cart_item_id)
#     cart_list.delete()
#     print(cart_item_id)
#     return redirect('cart')

@login_required
def remove_from_cart(request, cart_item_id):
    try:
        cart_item_id = int(cart_item_id)
        cart_item = get_object_or_404(cart, id=cart_item_id)
        cart_item.delete()
        return redirect('cart')
    except cart.DoesNotExist:
        error_message = "Failed to remove item from cart. Please try again later."
        return render(request, 'cart.html', {'error_message': error_message})
    except ValueError:
        error_message = "Invalid cart item ID."
        return render(request, 'cart.html', {'error_message': error_message})


@user_passes_test(lambda user: user.is_superuser, login_url='/')
def home_list(request):
    low_prices = 0
    middle_prices = 0
    high_prices = 0

    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('error')

    for home in HomeDcor.objects.all():
        if '0' <= str(home.price) <= '15':
            low_prices += 1
        elif '16' <= str(home.price) <= '40':
            middle_prices += 1
        else:
            high_prices += 1

    return render(request, 'Chart.html', {'low_prices': low_prices, 
	'middle_prices': middle_prices, 
	'high_prices': high_prices, })






# @user_passes_test(lambda user: user.is_superuser)
# def home_list(request):
#     low_prices = 0
#     middle_prices = 0
#     high_prices = 0


#     for home in HomeDcor.objects.all():
#         if '0' <= str(home.price) <= '15':
#             low_prices += 1
#         elif '16' <= str(home.price) <= '40':
#             middle_prices += 1
#         else:
#             high_prices += 1

#     return render(request, 'Chart.html', {'low_prices': low_prices, 
# 	'middle_prices': middle_prices, 
# 	'high_prices': high_prices, })







