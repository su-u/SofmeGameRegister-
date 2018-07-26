from django.db import models
from datetime import datetime
from django.contrib import admin
from django.core.validators import ValidationError
import uuid

#FILE_PATH = "gameregister/static/gameregister"
FILE_PATH = ""

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
    def uuid_validation(value):
        #if len(value) == 0:
        #    raise ValidationError("未入力")
        if(len(str(value)) == 0) or value == None:
            raise ValidationError("a")

    game_id = IntegerRangeField("GameID", default = 1, primary_key = True, help_text='1~100', min_value=1, max_value=100)
    name = models.CharField("名前", max_length = 100, help_text = '100文字以下')
    representative = models.CharField("企画者", max_length = 100, help_text = "100文字以下")
    discription = models.TextField()

    windows = models.BooleanField("Windows端末", blank = True)
    android = models.BooleanField("Android端末", blank = True)
    vr = models.BooleanField("VR", blank = True)
    other = models.BooleanField("その他独自筐体", blank = True)


    
    game_uuid = models.UUIDField(primary_key = False, default = uuid.uuid4, editable=False)

    gamefile = models.FileField(upload_to = FILE_PATH + "gamefile", blank = True)

    panel = models.FileField(upload_to = FILE_PATH + "panel", blank = True)

    picture_1 = models.FileField(upload_to = FILE_PATH + "picture", blank = True)
    picture_2 = models.FileField(upload_to = FILE_PATH + "picture", blank = True)
    picture_3 = models.FileField(upload_to = FILE_PATH + "picture", blank = True)

    movie = models.FileField(upload_to = FILE_PATH + "movie", blank = True)

    created_at = models.DateTimeField("作成時", auto_now_add = True)
    updated_at = models.DateTimeField("更新時", auto_now = True)

    edit_uuid = models.CharField("UUID", max_length = 40, help_text = "40文字以下", blank = True, validators = [uuid_validation])

    def __str__(self):
        return str(self.game_uuid)
   


class Log(models.Model):
 
    ip = models.GenericIPAddressField()
    access_at = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey(GameInfo)
 
    def __str__(self):
        return "{0},{1}".format(self.ip, self.access_at)