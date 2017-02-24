# coding=utf-8
from django.shortcuts import render
from homepage.models import Homepagedb, Userdb
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django import forms


def index(req):
    context = {}
    #尝试查库
    m = Userdb.objects.get(username="xuchu")
    print m.username, ":", m.password
    # print req.session.keys()
    # print req.session.items()
    # print req.session.get_expiry_date()
    username = req.session.get('username', '请登录哦')
    context['username'] = username
    response = render(req, "index.html", context=context)
    response["location"] = "/index"
    return response


def show_homepagedb(req):
    """试验读库"""
    db_list = Homepagedb.objects.all()
    # print db_list
    return render(req, "show_homepagedb.html", {'db_list': db_list})


class UserForm(forms.Form):
    username = forms.CharField(max_length=10)


def login(req):
    """主站登陆html"""
    context = {}
    context['title'] = 'Login'
    return render(req, "login.html", context=context)


def login_req(req):
    """主站登陆判断"""
    if req.method == "POST":
        username, password = req.POST['email'], req.POST['password']
        if username == "xuchu" and password == "1":
            result = "200"
            req.session['username'] = username
            req.session['result'] = result
            print req.session.items()
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
            return HttpResponseRedirect('/')
            # context = {}
            # context['username'] = username
            # return render(req, "login_t.html", context=context)
    else:
        uf = UserForm()
    return render(req, 'login_t.html', {'uf': uf})


# 登陆后跳转页
def login_index(req):
    username = req.session.get('username', '请登录哦')
    return render(req, 'login_index.html', {'username': username})


# 注销动作
def logout(req):
    del req.session['username']  # 删除session
    context = {}
    context['uf'] = UserForm()
    context['logout_succsess'] = 'logout_succsess'

    return render(req, 'login_t.html', context=context)
    # return HttpResponseRedirect('/')
    # return render(req, "login_index.html", context=context)
