from django.contrib import admin
from .models import Venues


class VenuesAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'added', 'url', 'email')


admin.site.register(Venues, VenuesAdmin)
