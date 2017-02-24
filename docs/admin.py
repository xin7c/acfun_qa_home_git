from django.contrib import admin
from .models import Docsdb, Teambuildingdb


class DocsdbAdmin(admin.ModelAdmin):
    list_display = ('id', 'doc_name', 'price', 'timestamp')


class DocsTeambuildingAdmin(admin.ModelAdmin):
    list_display = ('id', 'qa_name', 'sex' ,'go_where', 'comments', 'timestamp')
    list_display_links = ('id', "qa_name", 'sex', 'go_where', 'comments', 'timestamp')


admin.site.register(Docsdb, DocsdbAdmin)
admin.site.register(Teambuildingdb, DocsTeambuildingAdmin)
