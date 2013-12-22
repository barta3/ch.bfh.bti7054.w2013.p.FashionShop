from django.shortcuts import render
from products.models import ProductCategory, Product
from django.http.response import HttpResponseRedirect
from checkout.views import _addCartInfos
from checkout.models import ShoppingCart, Order, OrderForm, STATE_NEW

def index(request):
    context = { }
    addCategories(context)
    _addCartInfos(context, request)
        
    return render(request, 'home/index.html', context)


def productListByCategory(request, cat_name):
    prod_list = Product.objects.filter(category__name=cat_name)
    context = {'prod_list' : prod_list}
    
    addCategories(context)
    _addCartInfos(context, request)

    return render(request, 'home/prodlist.html', context)

def productDetail(request, cat_name, prod_id):
    context = { }
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            _addToCart(request, cat_name, prod_id, form.cleaned_data['size'])
            return HttpResponseRedirect('/home/')
    else:
        form = OrderForm()
        context ['prod'] = Product.objects.get(id=prod_id)
        addCategories(context)
        _addCartInfos(context, request)
        
    context['form'] = form
    return render(request, 'home/productDetail.html', context)

def _addToCart(request, cat_name, prod_id, size):
    
    cartByUser = ShoppingCart.objects.get_or_create(user=request.user, state=STATE_NEW)[0]
     
    order = Order.objects.create(product=Product.objects.get(id=prod_id))
    order.size = size
    order.save()
     
    cartByUser.orders.add(order)
    
    return HttpResponseRedirect('/home/')
    

def addCategories(context):
    cat_list = ProductCategory.objects.all()
    context['cat_list'] = cat_list

