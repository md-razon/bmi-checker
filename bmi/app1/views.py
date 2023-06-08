from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST' :
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!= pass2:
            return HttpResponse("Your password and confirm password are not same.")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
        

        return redirect('login')

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incoreect!!!")
        

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('signup')    



def calc(request):
    return render(request,"home.html") 

def process(request):
    wt=float(request.GET["weight"])
    ht=float(request.GET["height"])
    bmi=(wt*100*100)/(ht*ht)

    category=["underweight","normal","overweight","obesity"]
    if bmi<18.5:
        result=category[0]
    elif bmi>=18.5 and bmi<=24.9:
        result=category[1]
    elif bmi>=25.0 and bmi<=29.9:
        result=category[2]
    else:
         result=category[3]
    params={"value":bmi,"what":result}

    return render(request,'process.html',params)


def IndexPage(request):
    return render(request,"index.html")

def Process1Page(request):
    return render(request,"process1.html")

def calc(request):
    return render(request,"index.html") 

def Process1Page(request):
    hti=float(request.GET["heightinch"])
    result1=(hti*2.54)
    params1={"value1":result1}
    return render(request,'process1.html',params1)



def BasePage(request):
    if request.method=='POST' :
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        bmi_result=request.POST.get('bmi_result')
        
        Userdata=User.objects.create_user(first_name,last_name,bmi_result)
        Userdata.save()

        return redirect('home')

    return render (request,'base.html')
