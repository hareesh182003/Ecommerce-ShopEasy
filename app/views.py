from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from app.forms import *
from django.core.mail import send_mail
from datetime import datetime,timedelta
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import random


def registration(request):
    EUFO = UserMF()
    EPFO = ProfileMF()
    if request.method == 'POST' and request.FILES:
        NMUFDO = UserMF(request.POST)
        NMPFDO = ProfileMF(request.POST,request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            
            MUFDO = NMUFDO.save(commit=False)
            pwd = NMUFDO.cleaned_data['password']
            MUFDO.set_password(pwd)
            MUFDO.save()

            MPFDO = NMPFDO.save(commit=False)
            MPFDO.username = MUFDO
            MPFDO.save()


            current_datetime = datetime.now()
            current_date = current_datetime.strftime("%Y-%m-%d")
            current_time = current_datetime.strftime("%H:%M:%S")
            
            
            send_mail(
            'Registration Of ShopEasy',
            f"""
Hi {MPFDO.first_name},

You have successfully logged into your ShopEasy account on {current_date} at {current_time}.

If this was you, no further action is needed. If you suspect any unauthorized access, please reset your password immediately or contact our support team.

Happy Shopping,  
The ShopEasy Team

""",
            'hareeshgarisha@gmail.com',
            [MUFDO.email],
            fail_silently=True
            )
            
            return render(request,'app/registration.html',{'EUFO':EUFO,'EPFO':EPFO,'success':'Registration is Done Successfully'})
        else:
            return HttpResponse('invalid')

    return render(request,'app/registration.html',{'EUFO':EUFO,'EPFO':EPFO})

def home(request):
    if request.session.get('username'):
        username = request.session.get('username')
        return render(request,'app/home.html',{'username1':username})
    return render(request,'app/home.html')


@login_required
def profilePage(request):
    username = request.session.get('username')
    UO = User.objects.get(username=username)
    PO = Profile.objects.get(username=UO)
    d = {'UO':UO,'PO':PO}
    return render(request,'app/sample.html',d)




def otpgenerator():
    return random.randint(100000,999999)

def otp_page(request):
    
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        otp = request.session.get('otp')
        otp_source = request.session.get('otp_source')
        otp_expiry = request.session.get('otp_expiry')

        if otp_expiry and datetime.now() > datetime.strptime(otp_expiry, '%Y-%m-%d %H:%M:%S'):
            return render(request, 'app/otp_page.html', {'error': 'OTP has expired. Please try again.'})

        if entered_otp and int(entered_otp) == otp:
            if otp_source == 'login' or otp_source == 'loginresendOTP':
                return redirect('login_continue')

            elif otp_source == 'reset' or otp_source == 'resetresendOTP':
                return redirect('reset_continue')
        else:
            return HttpResponse('Invalid OTP')
    return render(request,'app/otp_page.html')

    

def loginPage(request):
    ELF = UserLoginForm()
    if request.method == 'POST':
        ELFDO = UserLoginForm(request.POST)
        if ELFDO.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            AUO = authenticate(username=username,password=password)
            if AUO and AUO.is_active:
                otp = otpgenerator()
                UO = User.objects.get(username= username)
                send_mail(
                    'Login OTP',
f"""
Dear {username},

Your ShopEasy login OTP is {otp}. This OTP is valid for the next 2 minutes.

Please do not share this OTP with anyone. If you did not request this, please contact our support team immediately.

Thank you,
The ShopEasy Team
""",
                    'hareeshgarisha@gmail.com',
                    [UO.email],
                    fail_silently=False
                          )
                request.session['otp'] = otp
                request.session['username'] = username
                request.session['password'] = password
                request.session['otp_source'] = 'login'
                request.session['otp_expiry'] = (datetime.now() + timedelta(minutes=2)).strftime('%Y-%m-%d %H:%M:%S')
                return redirect('otp_page')
            else:
                return HttpResponse('Invalid User')
    return render(request,'app/loginPage.html',{'ELF':ELF})


def login_continue(request):
    if request.session.get('username'):
        username = request.session.get('username')
        password = request.session.get('password')
        AUO = authenticate(username = username,password=password)
        login(request,AUO)
        request.session['username'] = username
        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponse('Invalid user')

@login_required
def Userlogut(request):
    logout(request)
    EULF = UserLoginForm()
    return render(request,'app/loginPage.html',{'EULF':EULF})

# @login_required
# def product_list(request):
#     if request.method == 'POST':
#         category_filter = request.POST.get('category', '')
#         if category_filter:
#             products = Product.objects.filter(category__icontains=category_filter)
#         else:
#             products = Product.objects.all()
#         return render(request, 'app/product_list.html', {'products': products})








@login_required
def productItem(request):
    EPF = ProductMF()
    if request.method == 'POST':
        PFDO = ProductMF(request.POST)
        if PFDO.is_valid():
            PFDO.save()
            return render(request,'app/productItem.html',{'EPF':EPF,'success':'Product Added Successfully'})
    return render(request,'app/productItem.html',{'EPF':EPF})
    









def resendOTP(request):
    resendotp = otpgenerator()

    username = request.session.get('username')
    UO = User.objects.get(username=username)

    send_mail(
                    'Login OTP',
f"""
Dear {username},

Your ShopEasy login OTP is {resendotp}. This OTP is valid for the next 2 minutes.

Please do not share this OTP with anyone. If you did not request this, please contact our support team immediately.

Thank you,
The ShopEasy Team
""",
                    'hareeshgarisha@gmail.com',
                    [UO.email],
                    fail_silently=False
                          )
    request.session['otp'] = resendotp
    request.session['otp_source'] = 'loginresendOTP'
    request.session['otp_expiry'] = (datetime.now() + timedelta(minutes=2)).strftime('%Y-%m-%d %H:%M:%S')
    return redirect('otp_page')
    






def cart(request):
    return render(request,'app/cart.html')