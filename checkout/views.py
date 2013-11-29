from django.shortcuts import render
from checkout.models import ShoppingCart, STATE_NEW
import home

def overview(request):
    context = { }
    home.views.addCategories(context)
    _addCartInfos(context, request)
    return render(request, 'checkout/overview.html', context)


def _addCartInfos(context, request):
    cart = ShoppingCart.objects.filter(user=request.user.id, state=STATE_NEW)
    if(cart.count() > 0):
        cartItems = cart[0].orders.all()
        context['cartItems'] = cartItems
        
def confirmation(request):
    context = { }
    home.views.addCategories(context)
    
    cart = ShoppingCart.objects.filter(user=request.user.id, state=STATE_NEW)[0]
    cart.close()
    cart.save()
    
    return render(request, 'checkout/thanks.html', context)