from django.contrib import admin

from historia_olimpica.models import AthleteEvents, NocRegions


@admin.register(AthleteEvents)
class AthleteEventsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'games', 'year', 'sport', 'medal']


@admin.register(NocRegions)
class NocRegionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'noc', 'region', 'notes']
