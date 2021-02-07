from django.contrib import admin
from userManage.models import Role, User


# Register your models here.


class RoleAdmin(admin.ModelAdmin):
    list_display = ("id", "role_name", "role")


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "role")


admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
