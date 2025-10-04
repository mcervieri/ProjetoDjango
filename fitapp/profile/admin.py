from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"


class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "get_role",
    )

    def get_role(self, obj):
        return obj.profile.role if hasattr(obj, "profile") else "-"

    get_role.short_description = "Role"


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
