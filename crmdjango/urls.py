"""
URL configuration for crmdjango project.

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
from django.urls import path, include

from django.contrib.auth import views
from core.views import index, sobre
from userprofile.views import signup
from lead.views import add_lead

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('signup/', signup, name='signup'), ## APP USERPROFILE
    path('login/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'), ## APP USERPROFILE
    path('logout/', views.LoginView.as_view(), name='logout'), ## APP USERPROFILE
    path('dashboard/', include('dashboard.urls')), ## APP DASHBOARD
    path('dashboard/', include('lead.urls')), ## APP LEAD
    
]
