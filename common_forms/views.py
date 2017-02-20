# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm


def testform(req):
    form = AddForm()
    return render(req, "testform.html", {"form": form})

def testfrom_add(req):
    # print req.POST
    if req.method == "POST":
        form = AddForm(req.POST)
        if form.is_valid():
            print "表单验证[成功],合法数据:", form.cleaned_data
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            result = "%s : [%s]" %(str(int(a) + int(b)), c)
            print result
            return HttpResponse(result)
        else:
            print "表单验证[失败],合法数据:", form.cleaned_data
            return HttpResponse(None)