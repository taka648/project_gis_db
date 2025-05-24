# リスト3-3:datashare/urls.py
from django.urls import path
from . import views

app_name = "datashare"

urlpatterns = [
    # viewsの関数indexを紐付ける
    path(
        "", views.index, name="index"
    ),
    # リスト3-6:追加。viewsの関数mypageを紐付ける
    path(
        "mypage/", views.mypage_funView, name="mypage"
    ),
    # リスト3-14:追加。viewsの関数ではなくクラスであるので、frmPublishView.as_view()の記述でフォーラムクラスと紐付ける。
    path(
        "frmPublish/", views.frmPublishView.as_view(), name="frmPublish"
    ),
    # リスト4-14:追加。4.5.1 情報表示とファイルとダウンロードの機能実装、手順2:アプリdatashareのurls.pyの記述追加
    path(
        "mypage_db/", views.mypage_dbView.as_view(), name="mypage_db"
    ),
    # リスト4-18:追加。4.5.2 情報発信とファイルァップロードの機能実装、手順3:アプリdatashareのurls.pyの記述追加
    path(
        "publish_db/", views.publish_byModelfrmView, name="publish_db"
    ),
    # リスト4-22:追加。4.5.3 情報更新と削除の機能実装、手順2:アプリdatashare/urls.pyへの記述追加
    path(
        "edit/<int:num>", views.edit, name="edit"
    ),
    # リスト4-38:追加。4.6.2 アプリケーションdatashareにおけるユーザ認証機能の実装、手順4:
    # リスト4-38の行13と行14は、それぞれMyLoginViewとMyLogoutViewに対し、URLとビュークラスの紐付けを設定する。
    path(
        "login/", views.MyLoginView.as_view(), name = "login"
    ),
    path(
        #"logout/", views.MyLogoutView.as_view(), name= "logout"
        "logout/", views.MyLogoutView.as_view(), name= "logout"
    ),
]

