# coding=utf-8
from django.shortcuts import render
from homepage.models import Homepagedb
from django.http import HttpResponse, HttpResponseRedirect
from django import forms


def index(req):
    return render(req, "index.html", {})


def show_homepagedb(req):
    """试验读库"""
    db_list = Homepagedb.objects.all()
    # print db_list
    return render(req, "show_homepagedb.html", {'db_list': db_list})


class UserForm(forms.Form):
    username = forms.CharField()


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
    else:
        return HttpResponse("POST ONLY")


def login_t(req):
    if req.method == "POST":
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            # 把获取表单的用户名传递给session对象
            req.session['username'] = username
            return HttpResponseRedirect('/login_index/')
    else:
        uf = UserForm()
    return render(req, 'login_t.html', {'uf': uf})

#登陆后跳转页
def login_index(req):
    username = req.session.get('username', 'anybody')
    return render(req, 'login_index.html', {'username': username})

#注销动作
def logout(req):
    del req.session['username'] #删除session
    return HttpResponse('LogOut Done!')
