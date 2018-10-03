from django import forms
from .models import GameInfo

 
class GameInfoForm(forms.ModelForm):
    class Meta:
        model = GameInfo
        fields = ("name", "representative", "game_id", "discription", "windows", "android", "vr", "other",
                  "is_mouse", "is_gamepad", "is_keyboard",
                 "gamefile", "panel","picture_1","picture_2","picture_3" ,"movie")
        
        widgets = {
            "name": forms.TextInput(attrs={"placeholder":"ゲーム名"}),
            "representative": forms.TextInput(attrs={"placeholder":"企画者"}),
            "discription": forms.TextInput(attrs={"placeholder":"説明文","row":"2"}),
            "game_id": forms.TextInput(attrs={"placeholder":"GameID","type":"number"}),
            "edit_uuid": forms.TextInput(attrs={"placeholder":"UUID"}),
            #"gamefile": forms.FileInput(attrs={"onchange":"gamefiletext.style.display='inline-block'; gamefiletext.value = this.value;"}),
            #"panel": forms.FileInput(attrs={"onchange":"paneltext.style.display='inline-block'; paneltext.value = this.value;"}),
            #"picture_1": forms.FileInput(attrs={"onchange":"picture_1text.style.display='inline-block'; picture_1text.value = this.value;"}),
            #"picture_2": forms.FileInput(attrs={"onchange":"picture_2text.style.display='inline-block'; picture_2text.value = this.value;"}),
            #"picture_3": forms.FileInput(attrs={"onchange":"picture_3text.style.display='inline-block'; picture_3text.value = this.value;"}),
            #"movie": forms.FileInput(attrs={"onchange":"movietext.style.display='inline-block'; movietext.value = this.value;"}),
        }

class EditForm(forms.Form):
    edit_uuid = forms.UUIDField(label = "識別UUID", max_length=40)
