"""
URL configuration for table project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from country.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_co/',insert_co,name='insert_co'),
    path('insert_ca/',insert_ca,name='insert_ca'),
    path('display_country/',display_country,name='display_country'),
    path('display_capital/',display_capital,name='display_capital'),

]
