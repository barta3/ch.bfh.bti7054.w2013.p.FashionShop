from django.shortcuts import render
from products.models import ProductCategotry

def index(request):
    cat_list = ProductCategotry.objects.all()
    context = { 'cat_list' : cat_list}
    return render(request, 'home/index.html', context)


