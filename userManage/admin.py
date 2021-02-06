from django.contrib import admin
from userManage.models import Role, User


# Register your models here.


class RoleAdmin(admin.ModelAdmin):
    list_display = ("id", "role_name", "role")


admin.site.register(User)
admin.site.register(Role, RoleAdmin)
