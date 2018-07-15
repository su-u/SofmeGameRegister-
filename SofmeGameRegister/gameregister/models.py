from django.db import models
from datetime import datetime
from django.contrib import admin
from django import forms
import uuid


# Create your models here.

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {"min_value": self.min_value, "max_value":self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class GameInfo(models.Model):
    game_id = IntegerRangeField("ゲームid", default = 1, primary_key = True, help_text='1~100', min_value=1, max_value=100)
    name = models.CharField("名前", max_length = 100, help_text = '100文字以下')
    representative = models.CharField("企画者", max_length = 100, help_text = "100文字以下", blank = True)
    discription = models.TextField()
    
    game_uuid = models.UUIDField(primary_key = False,default = uuid.uuid4, editable=False)

    gamefile = models.FileField(upload_to = "gamefile", blank = True)

    panel = models.FileField(upload_to = "panel", blank = True)

    picture_1 = models.FileField(upload_to = "picture", blank = True)
    picture_2 = models.FileField(upload_to = "picture", blank = True)
    picture_3 = models.FileField(upload_to = "picture", blank = True)

    movie = models.FileField(upload_to = "movie", blank = True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.game_uuid)


class AccessLog(models.Model):
    game_uuid = models.UUIDField(primary_key = False)
    ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
