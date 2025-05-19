# リスト3-12:datashare/templates/datashare/forms.py
from django import forms

class frmPublish(forms.Form):
    PROJECTS = (
       ('1', '地域防災関連'),
       ('2', '都市計画関連'),
       ('3', '地壌産婁関運'),
    )

    name = forms.CharField(label='Name', max_length=50)
    project = forms.ChoiceField(label='Project', choices=PROJECTS)
    contents = forms.CharField(label='Message', widget=forms.Textarea)
