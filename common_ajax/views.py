from django.shortcuts import render
from ajax_action import ssh_qa_server
from django.http import HttpResponse


def ajax_html(req):
    return render(req, "ajax.html", {})

def ajax_action(req):
    ssh_result = ssh_qa_server()
    return HttpResponse(ssh_result)