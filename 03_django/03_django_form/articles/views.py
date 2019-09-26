from IPython import embed
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404
from django.views.decorators.http import require_POST # post 요청만 받아준다..
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# Create your views here.
def index(request):
    articles = Article.objects.all() # model에서 meta로 ordering 미리 해줌...(이미 역순으로 가져온다)
    # articles = get_list_or_404(Article) # 글이 하나도 없으면 에러 뜸.....
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)

def create(request):
    # embed()
    if request.method == 'POST':
        # forms 작성 전
        # title instance
        # title = request.POST.get('title') # post로 들어오는 title 저장
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()

        # forms 작성 후
        # form 인스턴스를 생성하고 요청에 의한 데이터를 인자로 받는다.(binding 작업)
        # 이 처리과정은 binding이라고 불리며 유효성 체크를 할 수 있도록 해준다.
        form = ArticleForm(request.POST) # 인스턴스 생성(통째로 받아온다... -> FORM이 데이터에 맞춰서 알아서 매칭해줌)
        # form이 유효한지 체크한다.(유효성 검사)
        if form.is_valid():
            article = form.save() # 유효성 검사후 저장만 하면 된다(어느 필드에 있는지 model form을 쓰면 알게됨!)
            # form.cleaned_data로 정제된 데이터를 받는다.
            # title = form.cleaned_data.get('title') # 데이터 받아 저장.
            # content = form.cleaned_data.get('content')
            # 유효성 검사 끝났으므로..save 할 필요없이 바로 저장..
            # article = Article.objects.create(title=title, content=content)
        # return redirect('articles:index') # 글 작성되면  detail로... 
            return redirect(article) # get_absolute_url 작성하면 인스턴스 객체에 바로 넣을 수 있음
    else:
        form = ArticleForm() # 인스턴스 생성
    # 상황에 따라 context에 넘어가는 2가지 form
    # 1. GET: 기본 form
    # 2. POST: 검증에 실패 후의 form(is_valid == False)
    context = {'form': form,}
    return render(request, 'articles/form.html', context)  # get 방식일때...

def detail(request, article_pk):
    # try:
    article = get_object_or_404(Article, pk=article_pk) # 모델 객체, 인자(parameter)
    # except Article.DoesNotExist:    # DNE 에러 발생시 404에러 발생시키고 저 문구 띄워줌/
    #     raise Http404('No Article matches the given query.')
    comments = article.comment_set.all() # 모델명_set 으로 article 의 모든 댓글 가져온다!!
    comment_form = CommentForm()    # 댓글 폼(detail 에서 출력되야 하므로...여기 적어준다...)
    context = {'article': article, 'comment_form': comment_form, 'comments': comments,}
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')
 
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article) # request, instance 둘다 적어줘야함
        if form.is_valid():
            # model forms 설정하면 cleaned_data 필요없음!
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            article.save()
            return redirect(article)
    else:
        # ArticleForm 을 초기화 (이전에 DB에 저장된 데이터를 넣어준 상태)
        # form = ArticleForm(initial={'title': article.title, 'content': article.content,})# 이전 값들을 가져옴
        # __dict__ : article 객체 데이터를 딕셔너리 자료형으로 변환
        # form = ArticleForm(initial=article.__dict__)
        # model form쓰면 instance 로 이전 값 가져온다!!!
        form = ArticleForm(instance=article)
        
    # 1. POST : 검증에 실패한 form(오류 메세지도 포함된 상태)
    # 2. GET : 초기화된 form
    context = {'form': form, 'article': article,}
    return render(request, 'articles/form.html', context) # create랑 html 공유함!(둘 다 form을 사용하므로...)

@require_POST # post 요청만 허용하고 나머지는 막음...
            # if 문으로 post, get 분기할 필요 없음!!
def comments_create(request, article_pk):
    comment_form = CommentForm(request.POST) # 데이터 받아오기(인스턴스)
    # 유효성 검사
    if comment_form.is_valid():
        # commit=False
        # 객체를 create 하지만, db에 레코드는 작성하지 않는다.
        comment = comment_form.save(commit=False)
        comment.article_id = article_pk
        comment.save()
    return redirect('articles:detail', article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)