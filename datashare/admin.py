# リスト4-7:datashare/admin.py
from django.contrib import admin
from .models import pub_message

# 4.4.3 モデルのデータベース実装、手順1:必要な環境設定、(A)モデルの登録
# リスト4-7:追加。モデルpub_messageをアプリケーションdatashareに登録する
admin.site.register(pub_message)
