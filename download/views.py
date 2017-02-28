from django.shortcuts import render

def download(req):

    return render(req, 'download.html', {})