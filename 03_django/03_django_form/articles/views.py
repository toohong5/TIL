from IPython import embed
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST # post 요청만 받아준다..
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# Create your views here.
def index(request):
    # SESSION
    # 사용자가 사이트에 몇번 방문하는지 count 하기
    # session에 visits_num 키로 접근해 값을 가져온다.
    # 기본적으로 존재하지 않는 키이기 때문에 키가 없다면(방문한적이 없다면) 0 값을 가져오도록 한다.
    visits_num = request.session.get('visits_num', 0) # 해당 키(visits_num 가 없다면 새로 만들면서 0으로가져온다.
    # 그리고 가져온 값을 session에 visits_num에 매번 1 씩 증가한 값으로 할당한다. (유저의 다음 방문을 위해 count 누적시킴)
    request.session['visits_num'] = visits_num + 1
    # admin 에서 로그아웃 하고 다시 들어가면 이전 count가 누적 되지 않고 새롭게 count 된다.
    # 누적시키고 싶으면 "https://docs.djangoproject.com/en/2.2/topics/http/sessions/" 참고하기....
    # session data 안에 있는 새로운 정보를 수정했다면 django 는 수정한 사실을 알아채지 못하기 때문에 다음과 같이 설정한다.
    request.session.modified = True

    """
    visits_num = request.session.get('visits_num'. 0)
    request.session['visits_num'] = visits_num + 1
    request.session.modified = True
    """


    articles = Article.objects.all() # model에서 meta로 ordering 미리 해줌...(이미 역순으로 가져온다)
    # articles = get_list_or_404(Article) # 글이 하나도 없으면 에러 뜸.....
    context = {'articles': articles, 'visits_num': visits_num,}
    return render(request, 'articles/index.html', context)
    
@login_required # 로그인된 사람만 create로 접근가능함
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
    if request.user.is_authenticated: # 인증된 사용자만 delete 가능!!
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
    return redirect('articles:index')

@login_required
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

# @login_required # @login_required 와 @require_POST를 함께 쓰면 login 에서 next로 넘어갈때 GET방식으로 넘어가게 되어 405에러 발생함...
@require_POST # post 요청만 허용하고 나머지는 막음... / if 문으로 post, get 분기할 필요 없음!!
def comments_create(request, article_pk):
    if request.user.is_authenticated:
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
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
        return redirect('articles:detail', article_pk) # 인증된 사용자
    return HttpResponse('You are Unauthorized', status=401) # 인증안된 사용자 일때 (접근권한 없다는 에러 보여주기)