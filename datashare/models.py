# リスト4-6:datashare/models.py:pythonクラスとしてモデルを定義する。
from django.db import models
from django.contrib.auth.models import User, Group

# モデルpub_messageは、Djangoモデルクラスmodels.Modelを継承している。5つのフィールドを定義する。
# フィールドsenderは、外部キーフィールド(models.Foreign Key)として、Userテープルと関連付ける。
# 同じ方法で、フィールドprojectも外部キーとして、Groupテープルをつなぐ)。そのために、UserとGroupのモデルは、予めインプットしておく。
# フィールドsend_messageはmodels.CharFieldを用いて、文字列フィールドとして定義する。
# フィールドsend_documentはファイルアップロードをするために、models.Filefieldを使って定義する。
# 最後のsend_dateは投稿H付を保存するために、models.Date1Timeを用いて定義する。
class pub_message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Group, on_delete=models.CASCADE)
    send_message = models.CharField(max_length=1000)
    send_document = models.FileField(upload_to="documents/")
    send_date = models.DateTimeField(auto_now_add=True)
