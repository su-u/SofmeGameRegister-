from django.contrib import admin
from .models import GameInfo, Log, Tag


# Register your models here.
class TagInline(admin.TabularInline):
    model = GameInfo.tag.through 


class GameInfoAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at","game_uuid")
    list_display = ("game_id", "name","representative", "updated_at", "game_uuid", "windows", "android", "vr", "other",)
    inlines = [TagInline]
    exclude = ('tag',)
    search_fields = ("game_id", "name",)
    list_filter = ("windows", "android", "vr", "other", "is_mouse", "is_gamepad", "is_keyboard", "tag",)

class LogAdmin(admin.ModelAdmin):
    #readonly_fields = ("ip")
    readonly_fields = ("ip", "access_at", "access_type",)
    list_display = ("access_at_custom", "ip", "access_type")
    search_fields = ("access_type",)
    list_filter = ("access_type",)

class TagAdmin(admin.ModelAdmin):
    readonly_fields = ("tag_id",)
    list_display = ("tag_id", "tag_name", "color")

admin.site.register(GameInfo, GameInfoAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(Tag, TagAdmin)

def access_at_custom(self, obj):
    return obj.access_at_custom()