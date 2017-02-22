"""acfun_qa_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from homepage.views import index, show_homepagedb
from common_ajax.views import ajax_html, ajax_action
from docs.views import docs_html, docs_check_mysql, docs_Teambuilding
from common_forms.views import testform, testfrom_add

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^ajax/$', ajax_html, name="ajax_html"),
    url(r'^ajax/ajax_action$', ajax_action, name="ajax_action"),
    url(r'^docs/$', docs_html, name="docs_html"),
    url(r'^docs/docs_check_mysql$', docs_check_mysql, name="docs_check_mysql"),
    url(r'^docs/qatb$', docs_Teambuilding, name="docs_Teambuilding"),
    url(r'^testform/$', testform, name="testform"),
    url(r'^testform/testfrom_add/$', testfrom_add, name="testfrom_add"),
    url(r'^show_homepagedb/$', show_homepagedb, name="show_homepagedb"),
]
