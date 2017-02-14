from django.shortcuts import render

def docs_html(req):
    return render(req, "docs.html", {})