from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from checkout.models import ShoppingCart, STATE_ARCHIVE
from home.views import addCategories


def register(request, template_name='userauth/register.html', next_page_name=None):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if next_page_name is None:
                next_page = '/'
            else:
                next_page = reverse(next_page_name)
            return HttpResponseRedirect(next_page)
    else:
        form = UserCreationForm()
    return render_to_response(template_name, {'form': form},
        context_instance=RequestContext(request))
    
def archive(request):
    
    context = { }
    carts = ShoppingCart.objects.filter(user=request.user.id, state=STATE_ARCHIVE)
    context['cartItems'] = carts
    addCategories(context)
    
    
    return render(request, 'userauth/archive.html', context)