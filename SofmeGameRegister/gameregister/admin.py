from django.contrib import admin
from .models import GameInfo, Log


# Register your models here.
class GameInfoAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at","game_uuid")
    list_display = ("game_id", "name","representative", "updated_at")

class LogAdmin(admin.ModelAdmin):
    #readonly_fields = ("ip")
    list_display = ("access_at", "ip")

admin.site.register(GameInfo,GameInfoAdmin)
admin.site.register(Log,LogAdmin)
