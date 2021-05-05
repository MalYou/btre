from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'name', 'email', 'message', 'contact_date',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'listing', 'email',)
    list_per_page = 15

admin.site.register(Contact, ContactAdmin)
