"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home_redirect'),
    path('login/', views.login_view, name='login'),
    path('shop/', views.shop_view, name='shop'),
    path('home/', views.home, name='home'),
    
    path('men/', views.men_view, name='men'),
    path('women/', views.women_view, name='women'),
    path('kids/', views.kids_view, name='kids'),
    path('checkout/<str:product_name>/', views.checkout_view, name='checkout'),
    path('<str:category>/<str:product_name>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<str:category>/<str:product_name>/', views.add_to_cart, name='add_to_cart'),

    path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('thank-you/', views.thank_you, name='thank_you'),

]
