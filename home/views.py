from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Collections,Workings,Buying,Image

# Create your views here.
def home(request):
    imgs=Image.objects.all()

    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,'homepage.html',{'fname':'Admin', 'imgs':imgs})           
        else:
            fname=request.user.first_name.upper()
            return render(request,'homepage.html',{'fname':fname,'imgs':imgs})
    else:
        return render(request,'homepage.html',{'imgs':imgs})

def works(request):
    
    collects=Collections.objects.all()
    workings=Workings.objects.all()

    return render(request,'works.html',{'collects':collects, 'workings':workings})
        
def next(request):
    return render(request,'next.html',{'name':'next'})

def soon(request):
    return render(request,'comingsoon.html',{'name':'soon'})

def index(request):
    return render(request,'index.html')


def buy(request):

    if request.method == 'POST':
        buyername = request.POST['buyername']
        orderdescription = request.POST['description']
        phone_number = request.POST['phone_number']
        

        send=Buying()
        send.username  =request.user.username
        send.name=buyername
        send.order_description=orderdescription
        send.phone_number=phone_number
        send.save()

        return redirect('/')
    else:
        return render(request,'buy.html')

def myorders(request):
    if request.user.is_authenticated:
        ords=Buying.objects.all()
        no_orders=len(ords)==0
        num_orders_admin=len(ords)
        num_orders_user=0
        for ord in ords:
            if request.user.username==ord.username:
                num_orders_user+=1

        return render(request,'myorders.html',{'ords':ords, 'no_orders':no_orders,'num_orders_user':num_orders_user, 'num_orders_admin':num_orders_admin})
    else:
        return render(request,'login.html')

def gallery(request):
    images=Image.objects.all()
    return render(request,'gallery.html',{'images':images})