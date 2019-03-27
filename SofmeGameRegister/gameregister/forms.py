from django import forms
from .models import GameInfo
 
class GameInfoForm(forms.ModelForm):
    class Meta:
        model = GameInfo
        fields = ("name", "representative", "game_id", "display_id", "launcher_description", "signbord_description", "windows", "android", "vr", "other",
                 "is_mouse", "is_gamepad", "is_keyboard", "tag", "movie_2",
                 "game_manual", "gamefile", "panel","picture_1","picture_2","picture_3" ,"movie")
        
        widgets = {
            "name": forms.TextInput(attrs={"placeholder":"ゲーム名"}),
            "representative": forms.TextInput(attrs={"placeholder":"企画者"}),
            "launcher_description": forms.TextInput(attrs={"placeholder":"ランチャー用説明文","row":"2"}),
            "signbord_description": forms.TextInput(attrs={"placeholder":"プロジェクト看板用説明文","row":"2"}),
            "game_id": forms.TextInput(attrs={"placeholder":"GameID","type":"number"}),
            "display_id": forms.TextInput(attrs={"placeholder":"展示ID(入力不可)","type":"number", "readonly":"readonly"}),
            "edit_uuid": forms.TextInput(attrs={"placeholder":"UUID"}),
            "tag": forms.SelectMultiple(attrs={"class":"js-select2"}),
        }

class GameInfoFormEdit(forms.ModelForm):
    class Meta:
        model = GameInfo
        fields = ("name", "representative", "game_id", "display_id", "launcher_description", "signbord_description", "windows", "android", "vr", "other",
                 "is_mouse", "is_gamepad", "is_keyboard", "tag", "movie_2",
                 "game_manual", "gamefile", "panel","picture_1","picture_2","picture_3" ,"movie")
        
        widgets = {
            "name": forms.TextInput(attrs={"placeholder":"ゲーム名"}),
            "representative": forms.TextInput(attrs={"placeholder":"企画者"}),
            "launcher_description": forms.TextInput(attrs={"placeholder":"ランチャー用説明文","row":"2"}),
            "signbord_description": forms.TextInput(attrs={"placeholder":"プロジェクト看板用説明文","row":"2"}),
            "game_id": forms.TextInput(attrs={"placeholder":"GameID","type":"number", "readonly":"readonly"}),
            "display_id": forms.TextInput(attrs={"placeholder":"展示ID","type":"number", "readonly":"readonly"}),
            "edit_uuid": forms.TextInput(attrs={"placeholder":"UUID"}),
            "tag": forms.SelectMultiple(attrs={"class":"js-select2"}),
        }

class EditForm(forms.Form):
    edit_uuid = forms.UUIDField(label = "識別UUID", max_length=40)
