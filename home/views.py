from django.shortcuts import render
from products.models import ProductCategory, Product
from django.http.response import HttpResponseRedirect, HttpResponse
from checkout.views import _addCartInfos
from checkout.models import ShoppingCart, Order, OrderForm, STATE_NEW
import json
from django.db.models.query_utils import Q

def index(request):
    context = { }
    addCategories(context)
    _addCartInfos(context, request)
    
    context['showCase'] = Product.objects.filter(showcase=True)
        
    return render(request, 'home/index.html', context)


def productListByCategory(request, cat_name):
    prod_list = Product.objects.filter(category__name=cat_name)
    context = {'prod_list' : prod_list}
    
    addCategories(context)
    _addCartInfos(context, request)
    context['title'] = cat_name

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
        context['title'] =  Product.objects.get(id=prod_id).name
        
    context['form'] = form
    context['cat_name'] = cat_name
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
    
def search_prods(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        prods = Product.objects.filter(Q(name__icontains = q) |Q(desc__icontains = q))[:20]
        results = []
        for prod in prods:
            prod_json = {}
            prod_json['id'] = prod.id
            prod_json['label'] = prod.name
            prod_json['cat'] = prod.category.name
            results.append(prod_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


