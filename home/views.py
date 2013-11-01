from django.shortcuts import render
from products.models import ProductCategory, Product

def index(request):
    cat_list = ProductCategory.objects.all()
    context = { 'cat_list' : cat_list}
    return render(request, 'home/index.html', context)


def productListByCategory(request, cat_name):
    print("prodList View " + cat_name)
    prod_list = Product.objects.filter(category__name=cat_name)
    cat_list = ProductCategory.objects.all()
    context = {'prod_list' : prod_list, 'cat_list' : cat_list}
    return render(request, 'home/prodlist.html', context)

def productDetail(request, cat_name, prod_id):
    print("detail")
    context = {'prod' : Product.objects.get(id=prod_id), 'cat_list' : ProductCategory.objects.all()}
    return render(request, 'home/productDetail.html', context)