# coding=utf-8
from django.shortcuts import render
from homepage.models import Homepagedb
from django.http import HttpResponse


def index(req):
    return render(req, "index.html", {})

def show_homepagedb(req):
    """试验读库"""
    db_list = Homepagedb.objects.all()
    # print db_list
    return render(req, "show_homepagedb.html", {'db_list': db_list})

def login(req):
    """主站登陆html"""
    context = {}
    context['title'] = 'Login'
    return render(req, "login.html", context=context)

def login_req(req):
    """主站登陆判断"""
    if req.method == "POST":
        email, password = req.POST['email'], req.POST['password']
        if email == "xuchu" and password == "111111":
            result = u"登陆成功" + u"[" + email + u":" + password + u"]"
            return HttpResponse(result)
        else:
            result = "登录失败"
            return HttpResponse(result)
