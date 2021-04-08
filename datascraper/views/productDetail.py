from django.shortcuts import render,get_object_or_404
from datascraper.models import ProductModel


def productDetail(request,id):
    product = get_object_or_404(ProductModel)
   
    return render(request, 'pages/productDetail.html', context={
        'product' : product
    })

