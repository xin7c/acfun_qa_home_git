from django.shortcuts import render

def docs_html(req):
    '''docs html'''
    context = {}
    context["title"] = "Docs"
    return render(req, "docs.html", context=context)