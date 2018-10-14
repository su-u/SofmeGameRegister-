from django.contrib import admin
from .models import GameInfo, Log, Tag


# Register your models here.
#class TagInline(admin.TabularInline):
#    model = GameInfo.tag.through 


class GameInfoAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at","game_uuid")
    list_display = ("game_id", "name","representative", "updated_at", "game_uuid")
    #inlines = [TagInline]
    exclude = ('tag',)

class LogAdmin(admin.ModelAdmin):
    #readonly_fields = ("ip")
    readonly_fields = ("ip", "access_at", "access_type",)
    list_display = ("access_at", "ip", "access_type")

class TagAdmin(admin.ModelAdmin):
    readonly_fields = ("tag_id",)
    list_display = ("tag_id", "tag_name", "color")

admin.site.register(GameInfo, GameInfoAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(Tag, TagAdmin)
