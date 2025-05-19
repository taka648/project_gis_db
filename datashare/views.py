from django.shortcuts import render
from datashare.forms import frmPublish #リスト3-13:追加
from django.views.generic import TemplateView #リスト3-13:追加

def index(request):
    parmas = { 
        'title':'地理空間情報の共有サイト',
        'msg':'これはトッブページです。',
        'goto_mypage':'datashare:mypage', #リスト3-5:追加
    } 
    return render(request, 'datashare/index.html', parmas) 

# リスト3-5:追加
def mypage_funView(request):
    parmas = {
        'title': '地理空間情報の共有サイト',
        'msg': 'これはマイページです。',
        'goto_index': 'datashare:index',
    }
    return render(request,'datashare/mypage.html', parmas)

#リスト3-13:datashare/views.py:56-75
class frmPublishView(TemplateView):
    def __init__(self):
        self.parmas= {
            'title' : '地理空間情報の共有サイト',
            'msg' : 'これは、投稿ページです。',
            'form' : frmPublish(),
            'answer' : None,
            'goto_index' : 'datashare:index',
        } 

    def get(self, request):
        return render(request, 'datashare/frmPublish.html', self.parmas)

    def post(self, request):
        person = request.POST['name']
        proj = request.POST['project']
        cont = request.POST['contents']
        self.params['answer'] = 'name=' + person + ', project=' + proj + ',contents=' + cont+ '.'
        self.params['form'] = frmPublish(request.POST)
        return render(request, 'daashare/frmPublish.html',  self.parmas)
