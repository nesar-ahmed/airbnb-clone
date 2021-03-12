from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.
# admin.site.register(models.User, CustomUserAdmin)
@admin.register(models.User)
# class CustomUserAdmin(admin.ModelAdmin)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """

    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = ("language", "currency", "superhost")
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "birthdate",
                    "language",
                    "currency",
                    "bio",
                ),
            },
        ),
    )
