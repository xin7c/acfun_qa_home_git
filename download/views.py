# coding=utf8
from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.http import HttpResponse
import os
import acfun_qa_home.settings as settings


def download(req):
    file_list = [{"girl01": "girl01.png"}, {"g02": "g02.jpeg"},{"g03": "g03.jpg"}]
    context = {}
    context["file_list"] = file_list
    # context["girl01"] = "girl01.png"
    print context
    return render(req, 'download.html', context=context)


def big_file_download(req, c_path):
    # do something...
    print c_path
    print "下载资源链接:" + settings.STATICFILES_DIRS[0]

    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = c_path.encode('utf-8')
    # the_file_name_path = os.path.dirname(__file__) + "/files/" + the_file_name
    the_file_name_path = os.path.join(settings.STATICFILES_DIRS[0], the_file_name)

    response = StreamingHttpResponse(file_iterator(the_file_name_path))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response
