from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin

from users.models import User


# @admin.register(User)
# class CustomUserAdmin(admin.ModelAdmin):
#     pass

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthday",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
