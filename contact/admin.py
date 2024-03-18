from django.contrib import admin
from .models import Contact


# Register your models here.

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    list_display_links = ('id', 'name', 'email', 'created_at')
    search_fields = ['name', 'email']


admin.site.register(Contact)