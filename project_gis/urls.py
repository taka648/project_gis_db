# リスト4-9:project_gis/urls.py
from django.conf import settings  # リスト4-9:追加
from django.conf.urls.static import static  # リスト4-9:追加

# (2)手順2:ルーティングproject_gis/urls.pyの作成
from django.contrib import admin
from django.urls import path, include  # リスト3-2:includeを追加

urlpatterns = [
    path("admin/", admin.site.urls),
    path("datashare/", include("datashare.urls")),  # リスト3-2:追加
]

# リスト4-9:追加
# if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
