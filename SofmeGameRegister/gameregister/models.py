from django.db import models
from datetime import datetime
from django.contrib import admin


# Create your models here.
class GameInfo(models.Model):
    #file_name = models.CharField(max_length = 50)
    #upload_time = models.DateTimeField(default = datetime.now)
    name = models.CharField("名前", max_length = 255, help_text='255文字以下')
    id = models.IntegerField("id", default = 0, primary_key = True, help_text='0~50')
    discription = models.TextField()
    gamefile = models.FileField()

admin.site.register(GameInfo)
