# リスト4-9:project_gis/urls.py
from django.conf import settings  # リスト4-9:追加
from django.conf.urls.static import static  # リスト4-9:追加

# (2)手順2:ルーティングproject_gis/urls.pyの作成
from django.contrib import admin
from django.urls import path, include  # リスト3-2:includeを追加

urlpatterns = [
    path("admin/", admin.site.urls),
    path("datashare/", include("datashare.urls")),  # リスト3-2:追加
    path("account/", include('account.urls'))       # リスト4-28:追加。4.6.1 ユーザ認証のテスト実装、手順3:アプリケーションaccountへのpathを追加する
]

# 4.4.3 モデルのデータベース実装、手順2:ルーティングファイルヘの追記項目
# リスト4-9:追加。MEDIA_URLとMEDIA_ROOTへの紐付けを設定する。
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
