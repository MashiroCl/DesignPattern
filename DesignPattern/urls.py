"""DesignPattern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

import OnlineFastFood.views
import OnlineFastFood.customerEnd
import OnlineFastFood.businessEnd

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',OnlineFastFood.views.customerPage),
    path('commit/', OnlineFastFood.customerEnd.commit),
    path('host/',OnlineFastFood.views.admin_data),
    path('inform_takefood/',OnlineFastFood.businessEnd.inform_takefood),
    path('inform_kitchen/',OnlineFastFood.businessEnd.inform_kitchen),
    path('inform_phone/',OnlineFastFood.businessEnd.inform_phone),
    path('inform_text/',OnlineFastFood.businessEnd.inform_text),
    path('index/',OnlineFastFood.views.index),
    path('register/',OnlineFastFood.views.register),
    path('registerCheck/', OnlineFastFood.views.registerCheck),
    path('sign/',OnlineFastFood.views.sign),
    path('signCheck/',OnlineFastFood.views.signCheck),


]
