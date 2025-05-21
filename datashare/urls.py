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
    # リスト4-14:追加。4.5.1 情報表示とファイルとダウンロードの機能実装、手順
    path(
        "mypage_db/", views.mypage_dbView.as_view(), name="mypage_db"
    ),
    # リスト4-18:追加
    path(
        "publish_db/", views.publish_byModelfrmView, name="publish_db"
    ),
]
