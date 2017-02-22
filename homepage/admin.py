from django.contrib import admin
from .models import Homepagedb


class HomepadedbAdmin(admin.ModelAdmin):
    list_display = ('id', 'halo_text', 'sex', 'age')
    search_fields = ['id']
    # list_select_related = (True)
    list_display_links = ('id', 'age', 'halo_text', 'sex')


admin.site.register(Homepagedb, HomepadedbAdmin)
