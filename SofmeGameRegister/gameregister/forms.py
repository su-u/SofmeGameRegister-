from django import forms
from .models import GameInfo
 
class GameInfoForm(forms.ModelForm):
    class Meta:
        model = GameInfo
        fields = ["name", "representative", "game_id", "discription", "gamefile",
                 "panel","picture_1","picture_2","picture_3" ,"movie"]
        
        widgets = {
            "name": forms.TextInput(attrs={"placeholder":"ゲーム名"}),
            "representative": forms.TextInput(attrs={"placeholder":"企画者"}),
            "discription": forms.TextInput(attrs={"placeholder":"説明文","row":"2"}),
            "game_id": forms.TextInput(attrs={"placeholder":"GameID","type":"number"}),
        }

