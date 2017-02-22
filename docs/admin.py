from django.contrib import admin
from .models import Docsdb, Teambuildingdb

class DocsdbAdmin(admin.ModelAdmin):
    list_display = ('doc_name', 'price', 'timestamp')

class DocsTeambuildingAdmin(admin.ModelAdmin):
    list_display = ('qa_name', 'go_where', 'timestamp')

admin.site.register(Docsdb, DocsdbAdmin)
admin.site.register(Teambuildingdb, DocsTeambuildingAdmin)