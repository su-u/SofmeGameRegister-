from django.db import models
from datetime import datetime
from django.contrib import admin
from colorfield.fields import ColorField
from tinymce.models import HTMLField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
import os
import uuid
import urllib.parse

#FILE_PATH = "gameregister/static/gameregister"
FILE_PATH = ""


def upload_to_gamefile(instance, filename):
    return "{id}/gamefile/{file}".format(id=instance.game_id, file=filename)

def upload_to_panel(instance, filename):
    return "{id}/panel/{file}".format(id=instance.game_id, file=(filename))

def upload_to_pictures(instance, filename):
    return "{id}/pictures/{file}".format(id=instance.game_id, file=(filename))

def upload_to_movie(instance, filename):
    return "{id}/movie/{file}".format(id=instance.game_id, file=(filename))

def upload_to_manual(instance, filename):
    return "{id}/manual/{file}".format(id=instance.game_id, file=(filename))

#バリデーションチェック
def validate_is_game_manual(value):
    ext = os.path.splitext(value.name)[1]
    if not ext.lower() in [".pdf", ".PDF"]:
        raise ValidationError("拡張子が\"pdf\"ではありません。")

def validate_is_game_file(value):
    ext = os.path.splitext(value.name)[1]
    if not ext.lower() in [".zip", ".ZIP"]:
        raise ValidationError("拡張子が\"zip\"ではありません。")

def validate_is_pictures(value):
    ext = os.path.splitext(value.name)[1]
    if not ext.lower() in [".jpeg", ".JPEG", ".png", ".PNG", ".jpg", ".JPG"]:
        raise ValidationError("拡張子が\"jpg\",\"jpeg\",\"png\"ではありません。")

def validate_is_movies(value):
    ext = os.path.splitext(value.name)[1]
    if not ext.lower() in [".mp4", ".MP4", ".avi", ".AVI"]:
        raise ValidationError("拡張子が\"mp4\",\"avi\"ではありません。")

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


class GameInfo(models.Model):
    game_id = IntegerRangeField("GameID", default = 1, primary_key = True, help_text='1~500', min_value=1, max_value=500)
    display_id = IntegerRangeField("displayID", default = 1, help_text='1~500', min_value=1, max_value=500, blank = True, null = True)
    name = models.CharField("名前", max_length = 100, help_text = '100文字以下')
    representative = models.CharField("企画者", max_length = 100, help_text = "100文字以下")
    launcher_description = models.TextField("ランチャー用説明文", help_text = "100~160文字", validators=[MinLengthValidator(100)], max_length=160)
    signbord_description = models.TextField("プロジェクト看板用説明文", help_text = "20~80文字", validators=[MinLengthValidator(20)], max_length=80)

    windows = models.BooleanField("Windows端末", blank = True)
    android = models.BooleanField("Android端末", blank = True)
    vr = models.BooleanField("VR", blank = True)
    other = models.BooleanField("その他独自筐体", blank = True)

    is_mouse = models.BooleanField("マウス", blank = True)
    is_gamepad = models.BooleanField("ゲームパッド", blank = True)
    is_keyboard = models.BooleanField("キーボード", blank = True)

    game_uuid = models.UUIDField(primary_key = False, default = uuid.uuid4, editable=False)

    game_manual = models.FileField(upload_to = upload_to_manual, blank = True, validators=[validate_is_game_manual])

    gamefile = models.FileField(upload_to = upload_to_gamefile, blank = True, validators=[validate_is_game_file])
    gamefile_path = models.FilePathField(blank = True, null = True)

    #panel = models.FileField(upload_to = upload_to_panel, blank = True)
    panel = ProcessedImageField(upload_to = upload_to_panel,
                                processors=[ResizeToFill(800, 800)],
                                format='JPEG',
                                options={'quality': 90},
                                blank = True,
                                validators=[validate_is_pictures])
    
    #picture_1 = models.FileField(upload_to = upload_to_pictures, blank = True)
    picture_1 = ProcessedImageField(upload_to = upload_to_pictures,
                                processors=[ResizeToFill(1280, 720)],
                                format='JPEG',
                                options={'quality': 90},
                                blank = True,
                                validators=[validate_is_pictures])

    #picture_2 = models.FileField(upload_to = upload_to_pictures, blank = True)
    picture_2 = ProcessedImageField(upload_to = upload_to_pictures,
                                processors=[ResizeToFill(1280, 720)],
                                format='JPEG',
                                options={'quality': 90},
                                blank = True,
                                validators=[validate_is_pictures])

    #picture_3 = models.FileField(upload_to = upload_to_pictures, blank = True)
    picture_3 = ProcessedImageField(upload_to = upload_to_pictures,
                                processors=[ResizeToFill(1280, 720)],
                                format='JPEG',
                                options={'quality': 90},
                                blank = True,
                                validators=[validate_is_pictures])

    movie = models.FileField("ランチャー用動画", upload_to = upload_to_movie, blank = True, validators=[validate_is_movies])
    movie_2 = models.FileField("プレイ動画", upload_to = upload_to_movie, blank = True, validators=[validate_is_movies])

    created_at = models.DateTimeField("作成時", auto_now_add = True)
    updated_at = models.DateTimeField("更新時", auto_now = True)

    is_display = models.BooleanField("表示可能", default = True, blank = True)

    tag = models.ManyToManyField(Tag, verbose_name="タグ",blank = True)

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return u'%s' % (self.name)


class Log(models.Model):
    ip = models.GenericIPAddressField("IPアドレス")
    access_at = models.DateTimeField("アクセス時間", auto_now_add = True)
    access_type = models.CharField("アクセスタイプ", max_length = 100)
    post = models.ForeignKey(GameInfo, blank = True, null = True, on_delete=models.SET_NULL)
 
    def __str__(self):
        return "{0},{1}".format(self.ip, self.access_at)

    def access_at_custom(self, ):
        return "{0}/{1}/{2} {3}:{4}:{5}" \
            .format(self.access_at.strftime("%Y"), self.access_at.strftime("%m"), self.access_at.strftime("%d"), \
            self.access_at.strftime("%H"), self.access_at.strftime("%M"), self.access_at.strftime("%S")
            )

class HTMLbody(models.Model):
    page_id = models.IntegerField("PageID", primary_key = True)
    title = models.CharField(max_length=120, blank = True, null = True)
    description = models.TextField("ページの説明", max_length=250, blank = True, null = True)
    body = HTMLField(blank = True)

    def __str__(self):
        return self.title