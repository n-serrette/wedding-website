from django.contrib import admin

from .models import Guest, Party


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "is_child", "party"]


class GuestInline(admin.TabularInline):
    extra = 0
    model = Guest


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [GuestInline]
