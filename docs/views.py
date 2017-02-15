#coding=utf-8
from django.shortcuts import render
from homepage.models import Homepagedb
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

def docs_html(req):
    '''docs html'''
    context = {}
    context["title"] = "Docs"
    return render(req, "docs.html", context=context)

def docs_check_mysql(req):
    if req.method == "POST":
        post_id = req.POST["input_check_mysql"]
        max_id = Homepagedb.objects.values("id").last()["id"]
        print "Homepagedb中id最大值为[%d]" %max_id

        if post_id.isdigit() and 0 < int(post_id) <= max_id:
            text = Homepagedb.objects.get(id=post_id)
            print "查询成功:",post_id
            return HttpResponse(text)

        elif post_id.isdigit() and int(post_id) > max_id:
            print "查询失败:",post_id
            return HttpResponse(content="查询数据过大")
        
        else:
            return HttpResponse(content="Search Faild!!!")
        # try:
        #     text = Homepagedb.objects.get(id=post_id)
        #     print "查询成功:",text
        #     return HttpResponse(text)
        # except ObjectDoesNotExist:
        #     print ObjectDoesNotExist




