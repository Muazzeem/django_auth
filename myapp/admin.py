from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class JobCircularAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ["first_name"]
