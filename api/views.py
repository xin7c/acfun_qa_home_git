from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.views.decorators.vary import vary_on_headers
from django.utils.cache import patch_vary_headers
# Create your views here.
# @vary_on_headers('User-Agent', 'Cookie')
def api(req):

    session_items = req.session.items()
    print session_items
    print req.session.get_expiry_age()
    context = {}
    context['session_items'] = session_items
    context['COOKIES'] = req.COOKIES

    response = render(req, "api.html", context=context)
    response["qa"] = "1"
    response.set_cookie(key="isQa", value="isQa_value")
    response.set_cookie(key="isQa_1", value="isQa_value_1")
    return response