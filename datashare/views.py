from django.shortcuts import redirect, render #  リスト4-13:redirect追加
from datashare.forms import frmPublish, frmModelPublish # リスト4-13:frmModelPublish追加 # リスト3-13:追加
from django.views.generic import TemplateView # リスト3-13:追加
from .models import pub_message # リスト4-13:追加
from .forms import frmModelPublish # リスト4-17:追加

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

# リスト4-13:新規作成
class mypage_dbView(TemplateView):
    template_name = 'datashare/mypage_db.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pub_message_list'] = pub_message.objects.all().order_by('id')
         
        context['title'] = '地理空間データの共有サイト'
        context['msg'] = 'これはマイページ(DB接続)です'
        context['goto_index'] = 'datashare:index'
        return context

# リスト4-17:追加
def publish_byModelfrmView(request):
    if (request.method == 'POST'):
        form = frmModelPublish(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('datashare:mypage_db')
        else:
            form = frmModelPublish()

    parmas = {
        'title' : '地理空間情報の共有サイト',
        'msg' : 'これは投稿サイトです。',
        'form' : frmModelPublish(),
        'goto_mypage_db' : 'datashare:mypage_db', 
    } 
    return render(request, 'datashare/publish_db.html', parmas)
