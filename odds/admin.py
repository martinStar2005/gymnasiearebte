from django.contrib import admin

from .models import Match, Bookmaker, CurrentOdds, OddsHistory

admin.site.register(Match)
admin.site.register(Bookmaker)
admin.site.register(CurrentOdds)
admin.site.register(OddsHistory)