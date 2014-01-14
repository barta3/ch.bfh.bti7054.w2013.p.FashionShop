from django.shortcuts import render
from checkout.models import ShoppingCart, STATE_NEW
from django.core.mail import send_mail
from django.utils.translation import ugettext as _
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
    
    receipient = request.user.email
    
    msg = _("""
    Hello {0}, Thank you for your order.
    Total price: {1}
    Regards, Fahion Shop team""").format(request.user.first_name, cart.total())
    
    # Fail silently
    send_mail('Order Confirmation', msg, "info@fashioshop.com", [receipient], True)
    
    return render(request, 'checkout/thanks.html', context)