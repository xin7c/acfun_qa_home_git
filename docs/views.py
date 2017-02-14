from django.shortcuts import render

def docs_html(req):
    context = {}
    context["title"] = "Docs"
    print context
    return render(req, "docs.html", context=context)