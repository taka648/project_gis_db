# リスト4-7:datashare/admin.py
from django.contrib import admin
from .models import pub_message

admin.site.register(pub_message)  # リスト4-7:追加
