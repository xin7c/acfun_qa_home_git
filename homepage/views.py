# coding=utf-8
from django.shortcuts import render
from homepage.models import Homepagedb

def index(req):
    return render(req, "index.html", {})

def show_homepagedb(req):
    """试验读库"""
    db_list = Homepagedb.objects.all()
    # print db_list
    return render(req, "show_homepagedb.html", {'db_list': db_list})
