"""mysite URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
#from django.shortcuts import HttpResponse,render
from app01 import views

#def yimi(request):
    #request保存了所有和用户浏览器请求的相关数据

    #return HttpResponse("hello yimi")#需要自己到模块

    #自己找路径
    # open('templates/yimi.html','r', encoding="utf-8") as f:
    #    ret = f.read()
    #return HttpResponse(ret)

    #告诉Django自己找templates文件
#    return render(request, 'yimi.html')

urlpatterns = [
    url(r'^yimi/', views.yimi),
    url(r'^login/', views.login),
    url(r'^user_list/',views.user_list),
    url(r'^add_user/',views.add_user),
    url(r'^del_user/',views.del_user),
    url(r'^edi_user/',views.edi_user),
]

#Django的启动是右上角的三角向右的箭头标志