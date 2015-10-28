from django.contrib import admin

from .models import Link, Tag, List, UserProfile

class ListAdmin(admin.ModelAdmin):
	list_display = ('name', 'links', 'owner_name', 'is_public')
	list_editable = ('is_public')
	list_filter = ('is_public', 'owner_name')
	search_fields = ('name', 'links')
	readonly_fields = ('date_created', 'date_modified')

class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'name', 'owner', 'is_public', 'date_modified')
    list_editable = ('is_public',)
    list_filter = ('is_public', 'owner__username')
    search_fields = ['url', 'name', 'description']
    readonly_fields = ('date_created', 'date_modified')

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('name', 'verified')
	search_fields = ('name')
	readonly_fields = ('date_approval')

admin.site.register(UserProfile)
admin.site.register(Link)
admin.site.register(Tag)
admin.site.register(List)
