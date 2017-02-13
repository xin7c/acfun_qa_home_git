from django.shortcuts import render
from ajax_action import ssh_qa_server
from django.http import HttpResponse
import json

def ajax_html(req):
    return render(req, "ajax.html", {})

def ajax_action(req):
    if req.method == "POST":
        shell = req.POST[u'shell']
        print shell
        ssh_result = ssh_qa_server(command=shell)
        return HttpResponse(ssh_result)