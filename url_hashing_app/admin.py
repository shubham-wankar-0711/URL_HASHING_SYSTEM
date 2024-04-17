from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'key', 'created_at')  # display these fields in the list view
    list_filter = ('created_at',)  # add filters for these fields in the sidebar
    search_fields = ('address', 'key')  # add search box for these fields
    ordering = ('created_at', ) 

    def address(self, obj):
        return obj.full_address[:20]