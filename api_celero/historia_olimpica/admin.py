from django.contrib import admin

from historia_olimpica.models import AthleteEvents


@admin.register(AthleteEvents)
class AthleteEventsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'games', 'year', 'sport', 'medal']
