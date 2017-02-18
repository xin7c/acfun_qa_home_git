from django.shortcuts import render

def testform(req):
    current_path = req.get_host() + req.get_full_path()
    context = {}
    context["current_path"] = current_path
    return render(req, "testform.html", context=context)
