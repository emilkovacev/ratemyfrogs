from django.contrib import admin
from .models import Frog

class FrogAdmin(admin.ModelAdmin):
    search_fields = ['title', 'n']

admin.site.register(Frog, FrogAdmin)
