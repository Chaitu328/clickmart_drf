from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseAdmin
# Register your models here.
class UserAdmin(BaseAdmin):
    list_display = ['email','first_name','last_name','is_active']
    fieldsets = ()

admin.site.register(User)