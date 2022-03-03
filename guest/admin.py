from django.contrib import admin

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

from .models import Guest, Party

class GuestResource(resources.ModelResource):

	class Meta:
		model = Guest
		fields = ["first_name", "last_name", "attending_cocktail", "attending_dinner", "attending_brunch", "is_child", "party__name"]


@admin.register(Guest)
class GuestAdmin(ImportExportActionModelAdmin):
    list_display = ["first_name", "last_name", "is_child", "party"]
    resource_class = GuestResource

class GuestInline(admin.TabularInline):
    extra = 0
    model = Guest


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ['name', 'invitation_opened', 'response_received']
    inlines = [GuestInline]
