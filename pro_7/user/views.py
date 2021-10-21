from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
def reg(request):
    if request.method=='POST':
        username=request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pswrd = request.POST['pswrd']
        cpswrd = request.POST['pswrd1']
        if pswrd==cpswrd:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already used')
                return redirect('registration')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=pswrd)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'paswrd mismatch')
            return redirect('registration')
            print('user not created')
        return redirect('/')
    return render(request, "reg.html")
def login(request):
    if request.method=='POST':
        if request.method == 'POST':
            username = request.POST['user_name']
            pswrd = request.POST['pswrd']
            user=auth.authenticate(username=username,password=pswrd)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.info(request, 'user name or password incorrect')
                return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')