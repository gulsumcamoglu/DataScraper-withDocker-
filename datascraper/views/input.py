from __future__ import print_function
from django.shortcuts import render,redirect
from datascraper.forms import link
from datascraper.models import ProductModel
import mysql.connector




mydb = mysql.connector.connect(
    host ="db",
    user ="gulsum",
    password = "password",
    database = "my-app-db"
)



mycursor = mydb.cursor(buffered=True)




def input(request):
    import requests as r
    from bs4 import BeautifulSoup
    form = link()
    
    
    if request.method == 'POST':
        form = link(request.POST)
        if form.is_valid():
            getLink = form.cleaned_data['link']
            res = r.get(getLink)
            soup = BeautifulSoup(res.content,'html.parser')
            title = soup.select("h1.wt-text-body-03")
            
            name = title[0].get_text()
            name = name.replace(" ","")
            name = name.replace("\n","")
            strN = str(name)
            imgFrom = soup.find_all('img', class_='wt-max-width-full wt-horizontal-center wt-vertical-center carousel-image wt-rounded')
            img = str(imgFrom[0]['src'])
            
            price = soup.find_all('p',class_ = 'wt-text-title-03 wt-mr-xs-2')
            priceT = price[0].get_text()
            priceT = priceT.replace(" ","")
            priceT = priceT.replace("\n","")
            
            sql = "INSERT INTO product (id,name,img,price) VALUES (%s,%s,%s)"
            val = (name,img,priceT)
            mycursor.execute(sql,val)
            products = mycursor.execute("SELECT * FROM product")
            myresult = mycursor.fetchall()
            for i in myresult:
                print(i)
            mydb.commit()
            
            mydb.close()
            mycursor.close()
            
  
            return redirect('product')


    else:
         form = link()
    context = {
        'form':form
    }
    return render(request, 'pages/input.html', context=context)