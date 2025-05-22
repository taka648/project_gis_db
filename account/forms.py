# リスト4-28:新規作成。4.6.1 ユーザ認証のテスト実装、手順3:アプリケーションaccountへのpathを追加する
# ログインのフォームクラスLoginFormOを定義する。
# ここでは、リスト4-16と同じように、モデルを連携したフォームクラスを使用する。
# リスト4-16では、モデルpub_messageと連携したフォームクラスを定義するのに対し、
# リスト4-29はDjangoのユーザ管理モデルUserを使って(行2)、Userモデルのusernameとpasswordのフィールドを用いて、
# ログインフォームを定義する(行7)。また、フォームのひな型は、Djangoの認証フォーム「AuthenticationForm」を使用する(行1)。

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
 
class LoginForm(AuthenticationForm):
    class meta:
        model = User
        fields = ['username', 'password']
