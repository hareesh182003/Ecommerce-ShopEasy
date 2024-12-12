"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/',registration,name='registration'),
    path('',home,name='home'),
    path('loginPage/',loginPage,name='loginPage'),
    path('Userlogut/',Userlogut,name='Userlogut'),
    path('productItem/',productItem,name='productItem'),
    path('profilePage/',profilePage,name='profilePage'),
    path('otp_page/',otp_page,name='otp_page'),
    path('login_continue/',login_continue,name='login_continue'),
    path('resendOTP/',resendOTP,name='resendOTP'),
    path('cart/',cart,name='cart'),
    

    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
