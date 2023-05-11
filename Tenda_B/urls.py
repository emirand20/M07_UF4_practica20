"""Tenda_B URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home-
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from login.login import UserAPI
from rest_framework.authtoken import views
from login.views import Login, Logout
from payment.views import PagoView





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1.0/',include(('login.urls','login'))),
    path('api/1.0/create_user', UserAPI.as_view(), name="api_create_user"),
    path('api_generate_token/',views.obtain_auth_token),
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('payment/', PagoView.as_view(), name = 'payment'),
]


