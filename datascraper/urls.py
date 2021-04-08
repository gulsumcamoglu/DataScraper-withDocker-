from django.conf.urls import url
from datascraper.views import product,input,productDetail

urlpatterns = [
    url('',input,name = 'input'),
    url('product/',product, name = 'product'),
    url('productDetail/',productDetail, name= 'productDetail'),

]