from django.shortcuts import render
from datascraper.models import ProductModel
from django.core.paginator import Paginator
import mysql.connector

mydb = mysql.connector.connect(
    host ="db",
    user ="gulsum",
    password = "password",
    database = "my-app-db"
)
mycursor = mydb.cursor()

def product(request):
    products = mycursor.execute("SELECT * FROM product")
    page = request.GET.get('page')
    paginator = Paginator(products,2)

    return render(request, 'pages/product.html',context={
        'products':paginator.get_page(page)
    })

