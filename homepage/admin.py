from django.contrib import admin
from .models import Homepagedb, Userdb


class HomepadedbAdmin(admin.ModelAdmin):
    list_display = ('id', 'halo_text', 'sex', 'age')
    search_fields = ['id']
    # list_select_related = (True)
    list_display_links = ('id', 'age', 'halo_text', 'sex')

class UserdbAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'timestamp')
    list_display_links = ('id', 'username', 'password', 'timestamp')

admin.site.register(Homepagedb, HomepadedbAdmin)
admin.site.register(Userdb, UserdbAdmin)
