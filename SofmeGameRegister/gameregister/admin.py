from django.contrib import admin
from .models import GameInfo


# Register your models here.
class GameInfoAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at","game_uuid")
    list_display = ("game_id", "name","representative")

admin.site.register(GameInfo,GameInfoAdmin)
