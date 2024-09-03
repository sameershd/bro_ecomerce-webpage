from django.shortcuts import render,redirect
from . models import Order,OrderedtItem
from products.models import Product

# Create your views here.
def cart(request):
    return render(request,'cart.html')

def add_to_cart(request):
    if request.POST:
        user=request.user
        # customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        print('this is for showing id',product_id)
        cart_obj,created=Order.objects.get_or_create(
            owner=user,
            order_status=Order.CART_STAGE
        )
        product = Product.objects.get(pk=product_id)
        ordered_item=OrderedtItem.objects.create(
            product=product_id,
            owner=cart_obj,
            quantity=quantity
        )
    return redirect('cart')