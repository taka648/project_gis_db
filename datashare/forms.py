# リスト3-12:datashare/templates/datashare/forms.py
from django import forms
from .models import pub_message  # リスト4-16:追加
from django.contrib.auth.forms import AuthenticationForm # リスト4-36:追加。ログインフォームクラスLoginForm()を定義する
from django.contrib.auth.models import User #リスト4-36:追加。

# django.forms.Formクラスを継承し、フォームクラスfrmPublishを定義する。
# Djangoのフォームクラスを定義する構文の基本構造
# classフォームクラス名(forms.Form)
#     事前処理コード
#
#     変数名1 = forms.フィールドクラス1(引数1, 引数2, ...）
#     変数名2 = forms.フィールドクラス2(引数1, 引数2, ...）
#     ...
class frmPublish(forms.Form):
    PROJECTS = (
        ("1", "地域防災関連"),
        ("2", "都市計画関連"),
        ("3", "地壌産婁関運"),
    )
    # 3つのコンポーネント(部品)をform field classを用いて定義する。
    # 氏名を記述するtextbox:forms.CharFieldOのフィールドクラスを用いて定義し、変数nameに保存する。
    name = forms.CharField(label="Name", max_length=50)
    # 関辿プロジェクトを選択するためのdropdown list:変数projectとforms.ChoiceFeildOを用いて定義する。
    project = forms.ChoiceField(label="Project", choices=PROJECTS)
    # 、投稿メッセージを記入するためtextarea:forms.CharFieldOで定義し、引数widget=forms.Textareaを川いてテキストエリアを指定する。そのフィールドクラスは変数contentsで保仔される。
    contents = forms.CharField(label="Message", widget=forms.Textarea)


# リスト4-16:追加。
class frmModelPublish(forms.ModelForm):
    class Meta:
        model = pub_message
        fields = ["sender", "project", "send_message", "send_document"]

# リスト4-36:追加:4.6.2 アプリケーションdatashareにおけるユーザ認証機能の実装、手順1:
class LoginForm(AuthenticationForm):
    class meta:
        model = User
        fields = ['username', 'password']
