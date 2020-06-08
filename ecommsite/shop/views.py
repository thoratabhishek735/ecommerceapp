from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from .models import prodw
from .models import Contact
from .models import Orders
from .models import OrderUpdate

import json

from django.views.decorators.csrf import csrf_exempt

import math
MERCHANT_KEY = '380W#7mf&_SpEgsy'

# Create your views here.
def index(request):
    return render(request,'shop/index.html')
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    if(request.method == "POST"):
       name = request.POST.get('name','')
       email = request.POST.get('email','')
       phone = request.POST.get('phone','')
       message = request.POST.get('message','')
       print(name ,email, phone ,message)
       contact = Contact(name=name, email=email, phone=phone, message=message)
       contact.save()
       
    return render(request,'shop/contact.html')



def tracker(request):
    if(request.method=='POST'):
        orderId=request.POST.get('orderId','')
        email = request.POST.get('email','')

        try:
            order=Orders.objects.filter(order_id=orderId,email=email)
            print(order)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=orderId)
                print(update)
                updates=[]
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    print(order[0].items_json)
                    response = json.dumps({'status':"success",'updates':updates,'itemsjson':order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    
    return render(request,'shop/tracker.html')







def productview(request,myid):
    # fetch the product using id
    productss=prodw.objects.filter(id=myid)
   

    return render(request,'shop/prodview.html',{'product': productss[0]})



def productviewm(request,myidm):
    # fetch the product using id
    prod=product.objects.filter(id=myidm)
    print(myidm)
    print(prod)

    return render(request,'shop/prodviewm.html',{'product': prod[0]})


def checkout(request):
    if(request.method == "POST"):
       items_json=request.POST.get('itemsJson','')
       name = request.POST.get('name','')
       pamt = request.POST.get('amount','')
       email = request.POST.get('email','')
       phone = request.POST.get('phone','')
       address = request.POST.get('address','')
      
       city = request.POST.get('city','')
       state = request.POST.get('state','')
       zip_code = request.POST.get('zip_code','')
       
       order = Orders(items_json=items_json,name=name,pamt=pamt, email=email, phone=phone, address=address,city=city,state=state,zip_code=zip_code)
       order.save()
       update = OrderUpdate(order_id=order.order_id,update_desc="The order has been placed")
       update.save()
       thank = True
       id = order.order_id
      
       return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
      
    return render(request,'shop/checkout.html')


def mens(request):
    products = product.objects.all()
    
    
    params={'prod':products}
    return render(request,'shop/mens.html',params)



def womens(request):
    #Products = prodw.objects.all()
    #n = len(Products)
    #nslides= n//4 + math.ceil((n/4)-n//4)

    #params={'prd':Products,'no_of_slides': nslides,'range':range(1,nslides)}
    #allProds = [[Products,range(1,nslides),nslides],
     #          [Products,range(1,nslides),nslides]]
    allProds=[]
    catprods= prodw.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=prodw.objects.filter(category=cat)
        
        n=len(prod)
        nslides= n//4 + math.ceil((n/4)-n//4)
        allProds.append([prod,range(1,nslides),nslides])
    params={'allprods': allProds}
    return render(request,'shop/womens.html',params)



def searchmatch(query,item):
    #return true only if query matches the item
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    
    
    
    allpr = prodw.objects.all()
    allProds= [item for item in allpr if searchmatch(query,item) ]
    
        
    
    

    products = product.objects.all()
    productss = [item for item in products if searchmatch(query,item) ]
    
    
    params={'prod':productss,'allprods': allProds}
    if len(productss)==0 and len(allProds)==0:
        params={'msg':"Not Found search results please enter proper content"}
   
   
    return render(request,'shop/search.html',params)