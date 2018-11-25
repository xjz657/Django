from django.shortcuts import render

# Create your views here.
#专门用来存放函数

import pymysql
from jinja2 import Template
from django.shortcuts import HttpResponse,redirect#HttpResponse, render,
from app01 import models



def yimi(request):
    with open('E:\python\python\jinja2版web框架.html', 'r', encoding="utf-8") as f:
        ret = f.read()
    template = Template(ret)#生成模板文件
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='zgj189.',
        database='xue',
        charset='utf8',
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)#定义一个游标
    cursor.execute("select * from student;")#注意；号
    ret2 = cursor.fetchall()
    print(ret2)
    ret3 = template.render({'user_list': ret2})#把数据填充到模板里
    return HttpResponse(bytes(ret3, encoding="utf-8"))


def login(request):
    error_msg = ""
    if request.method == "POST":#必须大写
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        print(email, pwd)
        if "135@189.com" == email and "123456" == pwd:
            #return redirect("http://https://mail.163.com")#返回一个新链接
            return HttpResponse('登录成功')
        else:
            error_msg = "邮箱或密码错误"
    return render(request, "login.html", {"error": error_msg})


def user_list(request):
    #利用ORM查询数据库
    ret = models.UserInfo.objects.all()#排序.order_by("id")
    return render(request, "user_list.html", {"user_list":ret})#render(request, "use.html", {"user_list":ret})


def add_user(request):
    #PODT
    #用户填写了新用户名，发送POST请求
    error = ""
    if request.method == "POST":
        new_name = request.POST.get("username",None)
        if new_name:
            models.UserInfo.objects.create(name=new_name)
            #return HttpResponse("添加成功")
            return redirect("/user_list/")
        else:
            error = "提交的用户名字不能为空"
    return render(request, "add_user.html", {'error':error})


def del_user(request):
    #GET
    #用户填写了新用户名，发送POST请求
    del_id = request.GET.get("id",None)
    if del_id:
        del_obj = models.UserInfo.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/user_list/")
    else:
        return HttpResponse("要删除的数据不存在!")


def edi_user(request):
    # PODT
    # 用户填写了新用户名，发送POST请求
    error = ""
    if "GET" == request.method:
        user_id = request.GET.get("id", None)
        user = models.UserInfo.objects.get(id=user_id)
        return render(request, "edit_user.html",{"user":user})
    if "POST" == request.method:
        user_id = request.POST.get("id", None)
        user_name = request.POST.get("name", None)
        if user_id and user_name:
            user = models.UserInfo.objects.get(id=user_id)
            user.name = user_name
            user.save()
            return redirect("/user_list/")
        elif not user_id:
            user = models.UserInfo.objects.get(id=user_id)
            error = "要修改的用户不存在"
            return render(request, "edit_user.html", {'user':user,'error': error})
        elif not user_name:
            user = models.UserInfo.objects.get(id=user_id)
            error = "提交的用户名字不能为空"
            return render(request, "edit_user.html", {'user':user,'error': error})
    return render(request, "user_list.html")