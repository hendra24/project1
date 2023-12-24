from django.contrib import admin
from .models import Account, Profile
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'username', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'username')
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal= ()
    list_filter = ()
    fieldsets =  ()

    
admin.site.register(Account, AccountAdmin)


  
class ProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'company', 'city')


admin.site.register(Profile, ProfileAdmin)