# リスト3-3:datashare/urls.py
from django.urls import path
from . import views

app_name = 'datashare'

urlpatterns = [
   path('', views.index, name='index'),
   path('mypage/', views.mypage_funView, name='mypage'),                   # リスト3-6:追加
   path('frmPublish/', views.frmPublishView.as_view(), name='frmPublish'), # リスト3-14:追加
   path('mypage_db/', views.mypage_dbView.as_view(), name='mypage_db'),    # リスト4-14:追加
   path('publish_db/', views.publish_byModelfrmView, name='publish_db'),   # リスト4-18:追加
]
