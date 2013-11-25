from django.shortcuts import render
from checkout.models import ShoppingCart
import home

def overview(request):
    context = { }
    home.views.addCategories(context)
    _addCartInfos(context, request)
    return render(request, 'checkout/overview.html', context)


def _addCartInfos(context, request):
    cart = ShoppingCart.objects.filter(user=request.user.id)
    if(cart.count() > 0):
        cartItems = ShoppingCart.objects.filter(user=request.user.id)[0].orders.all()
        context['cartItems'] = cartItems