from django.contrib import admin
from . import models


admin.site.register(models.Category)



@admin.register(models.News)
class NewAdmin(admin.ModelAdmin):
	list_display = ["id", "title", "image", "created_time", "status",]
	list_filter = ["id", "slug", "status", "created_time"]
	prepopulated_fields = {"slug": ("title", )}
	search_fields = ("title",)


@admin.register(models.ContactAdmin)
class Contact(admin.ModelAdmin):
	list_display = ('name', 'email', 'create_time')
	search_fields = ("name", "email")