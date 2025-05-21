from django.shortcuts import redirect, render  #  リスト4-13:redirect追加
from datashare.forms import (
    frmPublish,
    frmModelPublish,
)  # リスト4-13:frmModelPublish追加 # リスト3-13:追加
from django.views.generic import TemplateView  # リスト3-13:追加。
from .models import pub_message  # リスト4-13:追加。、モデルpub_messageをインポートする。
from .forms import frmModelPublish  # リスト4-17:追加


def index(request):
    parmas = {
        "title": "地理空間情報の共有サイト",
        "msg": "これはトッブページです。",
        "goto_mypage": "datashare:mypage",  # リスト3-5:追加
    }
    return render(request, "datashare/index.html", parmas)


# リスト3-5:追加
def mypage_funView(request):
    parmas = {
        "title": "地理空間情報の共有サイト",
        "msg": "これはマイページです。",
        "goto_index": "datashare:index",
    }
    return render(request, "datashare/mypage.html", parmas)

# リスト3-13:datashare/views.py:56-75
# フォームクラスを処理するためのPythonクラスdjango.views.genericのビュークラス(view class:TemplateView)を使う。
# ビュークラスは、TemplateViewクラスを継承し、フォームクラスを処理する。
# ビュークラスの基本構造
# class クラス名(TemplateView):
#     def __init__(self): # 初期関数を定義し、必要があれば事前処理を行う。
#         [事前処理]
#
#     def get(self, ...)
#         関数getを定義し、フォームが最初に呼び出されるときの処理を行う。
#     def post(self, ...)
#         関数postを定義し、ユーザがフォームに何らかの情報を記述し、フォームが再びpostbackされたときの処理を行う。
# frmPublishViewクラスを追加する
class frmPublishView(TemplateView):
    def __init__(self):
        self.parmas = {
            "title": "地理空間情報の共有サイト",
            "msg": "これは、投稿ページです。",
            "form": frmPublish(),
            "answer": None,
            "goto_index": "datashare:index",
        }

    def get(self, request):
        return render(request, "datashare/frmPublish.html", self.parmas)

    def post(self, request): # ユーザがフォームに記述した情報requestを取得する。
        person = request.POST["name"]
        proj = request.POST["project"]
        cont = request.POST["contents"]
        # ユーザの回答を編集し、変数parmas['answer']へ渡す。
        self.parmas["answer"] = (
            "name=" + person + ", project=" + proj + ", contents=" + cont + "."
        )
        # フォームフィールドに記述情報が残されたままの状態で、フォームfrmPublish()を変数parmas['form']へ渡す。
        self.parmas["form"] = frmPublish(request.POST)
        # こうしたユーザ記述した惜報self.parmasをもう一度テンプレートのfrmPublish.htmlに送る。
        return render(request, "daashare/frmPublish.html", self.parmas)


# 4.5.1 情報表示とファイルとダウンロードの機能実装、手順1:アプリdatashareのviews.pyの記述追加
# リスト4-13:新規作成。クラスTemplateView継承したビュークラスmypage_dbViewを定義する。
# リスト3-13のクラスfrmPublishView()にもTemplateView継承したビュークラスを作成したが、今回のリスト4-13のクラス構造とは異なる。
# リスト3-13は、フォームと連動した動的な配信を対応するビュークラスであり、getとpostの2つの配信状態を踏まえ、
# __init__()、get()とpost()、3つの関数を設けた。
# それに対し、リスト4-13は、(1)モデルとの連動、(2)get関数による梢報収集のみであり、post関数による1青報の配信はない。
class mypage_dbView(TemplateView):
    # 紐付け先mypage_db.htmlのパスを明記する。
    template_name = "datashare/mypage_db.html"

    # データベースからデータの取得は、Djangoが用意したget_context_data()関数を利用する。
    # 親クラスから辞書型の引数**kwargsを持つget_context_data()関数を継承し、
    # 次のオーバーライド作業により、様々な情報を変数contextに渡す。
    # 行33では、pub_message.objects.all()を用いて、テープルpub_messageからすべてのデータを抽出し、その結果を
    # ["pub_message_list"] と名づけ、辞書型変数context["pub_message_list"]に渡す。
    # 次の行35～行37は、ページmypage_db.htmlに表示したい情報や、トップページindexへの名前空間URLを変数contextに渡す。
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pub_message_list"] = pub_message.objects.all().order_by("id")

        context["title"] = "地理空間データの共有サイト"
        context["msg"] = "これはマイページ(DB接続)です"
        context["goto_index"] = "datashare:index"
        return context


# リスト4-17:追加
def publish_byModelfrmView(request):
    if request.method == "POST":
        form = frmModelPublish(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("datashare:mypage_db")
        else:
            form = frmModelPublish()

    parmas = {
        "title": "地理空間情報の共有サイト",
        "msg": "これは投稿サイトです。",
        "form": frmModelPublish(),
        "goto_mypage_db": "datashare:mypage_db",
    }
    return render(request, "datashare/publish_db.html", parmas)


# リスト4-21:新規追加
def edit(request, num):
    obj = pub_message.objects.get(id=num)
    if request.method == "POST":
        if "btn_update" in request.POST:
            form = frmModelPublish(request.POST, instance=obj)
            form.save()
            return redirect("datashare:mypage_db")
        elif "btn_delete" in request.POST:
            obj.delete()
            return redirect("datashare:mypage_db")
        elif "btn_back" in request.POST:
            return redirect("datashare:mypage_db")

    parmas = {
        "title": "地理空間情報の共有サイト",
        "msg": "これは投稿の編集サイトです。",
        "id": num,
        "form": frmModelPublish(instance=obj),
    }

    return render(request, "datashare/edit.html", parmas)
