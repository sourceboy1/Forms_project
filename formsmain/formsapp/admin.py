from django.contrib import admin

# Register your models here.
from .models import FormData

class FormDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Display these fields in the list view
    search_fields = ('name', 'email')  # Add search functionality

admin.site.register(FormData, FormDataAdmin)
