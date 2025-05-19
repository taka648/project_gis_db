# リスト3-12:datashare/templates/datashare/forms.py
from django import forms
from .models import pub_message  # リスト4-16:追加


class frmPublish(forms.Form):
    PROJECTS = (
        ("1", "地域防災関連"),
        ("2", "都市計画関連"),
        ("3", "地壌産婁関運"),
    )

    name = forms.CharField(label="Name", max_length=50)
    project = forms.ChoiceField(label="Project", choices=PROJECTS)
    contents = forms.CharField(label="Message", widget=forms.Textarea)


# リスト4-16:追加
class frmModelPublish(forms.ModelForm):
    class Meta:
        model = pub_message
        fields = ["sender", "project", "send_message", "send_document"]
