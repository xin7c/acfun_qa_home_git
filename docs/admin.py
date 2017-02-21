from django.contrib import admin
from .models import Docsdb

class DocsdbAdmin(admin.ModelAdmin):
    list_display = ('doc_name', 'price', 'timestamp')


admin.site.register(Docsdb, DocsdbAdmin)