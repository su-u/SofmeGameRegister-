from django import forms
from .models import GameInfo
 
class GameInfoForm(forms.ModelForm):
    class Meta:
        model = GameInfo
        fields = ("name", "representative", "game_id", "display_id", "launcher_description", "signbord_description", "windows", "android", "vr", "other",
                  "is_mouse", "is_gamepad", "is_keyboard", "tag", "movie_2",
                 "gamefile", "panel","picture_1","picture_2","picture_3" ,"movie")
        
        widgets = {
            "name": forms.TextInput(attrs={"placeholder":"ゲーム名"}),
            "representative": forms.TextInput(attrs={"placeholder":"企画者"}),
            "launcher_description": forms.TextInput(attrs={"placeholder":"ランチャー用説明文","row":"2"}),
            "signbord_description": forms.TextInput(attrs={"placeholder":"プロジェクト看板用説明文","row":"2"}),
            "game_id": forms.TextInput(attrs={"placeholder":"GameID","type":"number"}),
            "display_id": forms.TextInput(attrs={"placeholder":"展示ID(入力不要)","type":"number", "readonly":"readonly"}),
            "edit_uuid": forms.TextInput(attrs={"placeholder":"UUID"}),
            "tag": forms.SelectMultiple(attrs={"class":"js-select2"}),
            #"gamefile": forms.FileInput(attrs={"onchange":"gamefiletext.style.display='inline-block'; gamefiletext.value = this.value;"}),
            #"panel": forms.FileInput(attrs={"onchange":"paneltext.style.display='inline-block'; paneltext.value = this.value;"}),
            #"picture_1": forms.FileInput(attrs={"onchange":"picture_1text.style.display='inline-block'; picture_1text.value = this.value;"}),
            #"picture_2": forms.FileInput(attrs={"onchange":"picture_2text.style.display='inline-block'; picture_2text.value = this.value;"}),
            #"picture_3": forms.FileInput(attrs={"onchange":"picture_3text.style.display='inline-block'; picture_3text.value = this.value;"}),
            #"movie": forms.FileInput(attrs={"onchange":"movietext.style.display='inline-block'; movietext.value = this.value;"}),
        }

class GameInfoFormEdit(forms.ModelForm):
    class Meta:
        model = GameInfo
        fields = ("name", "representative", "game_id", "display_id", "launcher_description", "signbord_description", "windows", "android", "vr", "other",
                  "is_mouse", "is_gamepad", "is_keyboard", "tag", "movie_2",
                 "gamefile", "panel","picture_1","picture_2","picture_3" ,"movie")
        
        widgets = {
            "name": forms.TextInput(attrs={"placeholder":"ゲーム名"}),
            "representative": forms.TextInput(attrs={"placeholder":"企画者"}),
            "launcher_description": forms.TextInput(attrs={"placeholder":"ランチャー用説明文","row":"2"}),
            "signbord_description": forms.TextInput(attrs={"placeholder":"プロジェクト看板用説明文","row":"2"}),
            "game_id": forms.TextInput(attrs={"placeholder":"GameID","type":"number", "readonly":"readonly"}),
            "display_id": forms.TextInput(attrs={"placeholder":"展示ID","type":"number", "readonly":"readonly"}),
            "edit_uuid": forms.TextInput(attrs={"placeholder":"UUID"}),
            "tag": forms.SelectMultiple(attrs={"class":"js-select2"}),
            #"gamefile": forms.FileInput(attrs={"onchange":"gamefiletext.style.display='inline-block'; gamefiletext.value = this.value;"}),
            #"panel": forms.FileInput(attrs={"onchange":"paneltext.style.display='inline-block'; paneltext.value = this.value;"}),
            #"picture_1": forms.FileInput(attrs={"onchange":"picture_1text.style.display='inline-block'; picture_1text.value = this.value;"}),
            #"picture_2": forms.FileInput(attrs={"onchange":"picture_2text.style.display='inline-block'; picture_2text.value = this.value;"}),
            #"picture_3": forms.FileInput(attrs={"onchange":"picture_3text.style.display='inline-block'; picture_3text.value = this.value;"}),
            #"movie": forms.FileInput(attrs={"onchange":"movietext.style.display='inline-block'; movietext.value = this.value;"}),
        }

class EditForm(forms.Form):
    edit_uuid = forms.UUIDField(label = "識別UUID", max_length=40)
