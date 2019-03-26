from django.contrib import admin
from .models import GameInfo, Log, Tag, HTMLbody
#from import_export.admin import ImportExportActionModelAdmin

admin.site.site_title = "ゲーム情報管理ページ"
admin.site.site_header = "ゲーム情報管理ページ"
admin.site.index_title = "メニュー"

# Register your models here.
class TagInline(admin.TabularInline):
    model = GameInfo.tag.through 


class GameInfoAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at","game_uuid")
    list_display = ("game_id", "display_id", "name","representative", "updated_at", "game_uuid", "is_display",)
    inlines = [TagInline]
    exclude = ('tag',)
    search_fields = ("game_id", "name",)
    list_filter = ("windows", "android", "vr", "other", "is_mouse", "is_gamepad", "is_keyboard", "tag", "is_display")
    ordering = ("game_id",)

#class LogAdmin(ImportExportActionModelAdmin):
class LogAdmin(admin.ModelAdmin):
    #readonly_fields = ("ip")
    readonly_fields = ("ip", "access_at", "access_type",)
    list_display = ("access_at_custom", "ip", "access_type")
    search_fields = ("access_type",)
    list_filter = ("access_type",)
    list_select_related = True
    date_hierarchy = "access_at"


class TagAdmin(admin.ModelAdmin):
    readonly_fields = ("tag_id",)
    list_display = ("tag_id", "tag_name", "color")
    ordering = ("tag_id",)

admin.site.register(GameInfo, GameInfoAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(HTMLbody)

def access_at_custom(self, obj):
    return obj.access_at_custom()