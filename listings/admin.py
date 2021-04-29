from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor', )
    list_display_links = ('id', 'title',)
    list_filter = ('realtor', )
    search_fields = ('title', 'address', 'state', 'price', )
    list_per_page = 15

admin.site.register(Listing, ListingAdmin)
