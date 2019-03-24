from django.db import models
from datetime import datetime
from django.contrib import admin
from django.core.validators import ValidationError
import uuid
from colorfield.fields import ColorField
import urllib.parse

#FILE_PATH = "gameregister/static/gameregister"
FILE_PATH = ""

# Create your models here.

class Tag(models.Model):
    tag_id = models.AutoField("TagID", primary_key=True)
    tag_name = models.CharField("TagName", max_length=100)
    color = ColorField("TagColor", default='#FFFFFF')

    def __str__(self):
        return str(self.tag_name)

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {"min_value": self.min_value, "max_value":self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

def upload_to_gamefile(instance, filename):
    return "{id}/gamefile/{file}".format(id=instance.game_id, file=filename)

def upload_to_panel(instance, filename):
    return "{id}/panel/{file}".format(id=instance.game_id, file=(filename))

def upload_to_pictures(instance, filename):
    return "{id}/pictures/{file}".format(id=instance.game_id, file=(filename))

def upload_to_movie(instance, filename):
    return "{id}/movie/{file}".format(id=instance.game_id, file=(filename))

class GameInfo(models.Model):
    game_id = IntegerRangeField("GameID", default = 1, primary_key = True, help_text='1~100', min_value=1, max_value=100)
    name = models.CharField("名前", max_length = 100, help_text = '100文字以下')
    representative = models.CharField("企画者", max_length = 100, help_text = "100文字以下")
    discription = models.TextField(help_text = "100~160文字")

    windows = models.BooleanField("Windows端末", blank = True)
    android = models.BooleanField("Android端末", blank = True)
    vr = models.BooleanField("VR", blank = True)
    other = models.BooleanField("その他独自筐体", blank = True)

    is_mouse = models.BooleanField("マウス", blank = True)
    is_gamepad = models.BooleanField("ゲームパッド", blank = True)
    is_keyboard = models.BooleanField("キーボード", blank = True)

    game_uuid = models.UUIDField(primary_key = False, default = uuid.uuid4, editable=False)

    gamefile = models.FileField(upload_to = upload_to_gamefile, blank = True)
    gamefile_path = models.FilePathField(blank = True, null = True)

    panel = models.FileField(upload_to = upload_to_panel, blank = True)
    
    picture_1 = models.FileField(upload_to = upload_to_pictures, blank = True)
    picture_2 = models.FileField(upload_to = upload_to_pictures, blank = True)
    picture_3 = models.FileField(upload_to = upload_to_pictures, blank = True)

    movie = models.FileField(upload_to = upload_to_movie, blank = True)
    movie_2 = models.FileField(upload_to = upload_to_movie, blank = True)

    created_at = models.DateTimeField("作成時", auto_now_add = True)
    updated_at = models.DateTimeField("更新時", auto_now = True)

    is_view = models.BooleanField(default = True, blank = True)

    tag = models.ManyToManyField(Tag, verbose_name="タグ",blank = True, null = True )

    def __str__(self):
        return str(self.game_uuid)

    def __unicode__(self):
        return u'%s' % (self.name)
   
class Log(models.Model):
    ip = models.GenericIPAddressField("IPアドレス")
    access_at = models.DateTimeField("アクセス時間", auto_now_add = True)
    access_type = models.CharField("アクセスタイプ", max_length = 100)
    post = models.ForeignKey(GameInfo, blank = True, null = True)
 
    def __str__(self):
        return "{0},{1}".format(self.ip, self.access_at)

    def access_at_custom(self, ):
        return "{0}/{1}/{2} {3}:{4}:{5}" \
            .format(self.access_at.strftime("%Y"), self.access_at.strftime("%m"), self.access_at.strftime("%d"), \
            self.access_at.strftime("%H"), self.access_at.strftime("%M"), self.access_at.strftime("%S")
            )


class ImageStandard(models.Model):
    pass

class MovieStandard(models.Model):
    pass