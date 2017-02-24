# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.vary import vary_on_headers
from django.utils.cache import patch_vary_headers
# @vary_on_headers('User-Agent', 'Cookie')
def api(req):
    session_items = req.session.items()
    print session_items
    # 打印过期时间
    # print req.session.get_expiry_age()
    context = {}
    context['session_items'] = session_items
    context['COOKIES'] = req.COOKIES

    response = render(req, "api.html", context=context)
    # 设置Response Headers
    response["location"] = "/api"
    response.set_cookie(key="isQa", value="isQa_value")
    return response