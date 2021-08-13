from .models import Note
from django.contrib import admin

# Register your models here.

admin.site.site_header = "Notes Administration"

class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'created', 'updated', 'completed', 'user']



admin.site.register(Note, NoteAdmin)
