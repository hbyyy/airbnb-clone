from django.contrib import admin

# Register your models here.
from users.models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    pass
