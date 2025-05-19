# (2)手順2:ルーティングproject_gis/urls.pyの作成
from django.contrib import admin
from django.urls import path, include # リスト3-2:includeを追加 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datashare/', include('datashare.urls')), # リスト3-2:追加
]
