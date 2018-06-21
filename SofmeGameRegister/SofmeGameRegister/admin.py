from django.contrib import admin
from gameregister.models import GameInfo




admin.site.register(GameInfo, GameInfoAdmin)