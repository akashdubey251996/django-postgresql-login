from django.shortcuts import render,redirect
from users.forms import RegisterForm,LoginForm
from users.backends import EmailBackend as em
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout

# Create your views here.



def home(request):
    return render(request,'users/home.html')


def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print('Successfull Registration')
            messages.success(request,"Thanks for successfull Registration")
            return redirect('/success')
    else:
        form = RegisterForm()
    
    return render(request,'users/register.html',{'form':form})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        uname = request.POST['username']
        pwd = request.POST['password']
        user = em.authenticate(username=uname,password=pwd)
        print(user)
        if user is not None:
            if user.is_active==True:
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                print(user)
                print('Successfull login')
                messages.success(request, f"You are now logged in {user}")
                return redirect ('/home')
        else:
            print('Unsuccessfull login')

    else:
        form = LoginForm()    
    return render(request,'users/login.html',{'form':form})


def gts(request):
    return render(request,'users/log-out.html')



def success(request):
    return render(request,'users/success.html',)

   


def user_logout(request):
    logout(request)
    return redirect('/user/logout/')
    
   
            