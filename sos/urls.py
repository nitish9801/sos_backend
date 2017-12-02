"""irelief_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from .views import *
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [

    # User creation
    url(r'^signup', SignUp.as_view(), name='signup'),
    url(r'^gcm', GoogleToken.as_view(), name='gcm'),

    url(r'^user', UserToken.as_view(), name='user'),

]
