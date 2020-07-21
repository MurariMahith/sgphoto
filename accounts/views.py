from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def login(request):

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Password wrong please try again')
            return redirect('/acc/login')
    else:
        return render(request,'login.html')

def signup(request):

    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        mobile_number=request.POST['mobile_number']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken... try with different username')
                return redirect('/acc/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already used')
                return redirect('/acc/signup')
            else:
                if len(mobile_number)==10:
                    user=User.objects.create_user(username=username,password=password1,first_name=first_name,email=email,last_name=last_name)
                    user.save()
                    return redirect('/acc/login')
                else:
                    messages.info(request,'please give valid mobile number')
                    return redirect('/acc/signup')


        else:
            messages.info(request,'Password not matching... retry registering')
            return redirect('/acc/signup')
        
        return redirect('/')

    else:
        return render(request,"signup.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def checkadmin(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/acc/adminbypass')
        else:
            return redirect('/')
    else:
        return redirect('/acc/login')


def adminbypass(request):
    admincode='alpha123'
    if request.method=='POST':
        given_admincode=request.POST['admincode']
        if given_admincode==admincode:
            return redirect('/admin')
        else:
            return redirect('/acc/adminbypass') 
    else:
        return render(request,'adminbypass.html') 

def users(request):
    users=User.objects.all()
    num_users=len(users)==0
    if request.user.is_superuser:
        return render(request,'users.html',{'users':users,'num_users':num_users})
    else:
        return redirect('/acc/login')
        