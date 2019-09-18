from IPython import embed # ipython
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect # POST에서는 URL을 직접 redirect 해줘야함
from .models import Article
# Create your views here.
def index(request):
    # 2 READ
    # 뒤집기 1. DB가 변경
    # 최신 글이 위로 올라오게(내림차순) DB가 변경!
    articles = Article.objects.order_by('-pk') 
    # 2. 파이썬이 변경
    # articles = Article.objects.all()[::-1]

    context = {'articles': articles,} # 전체글을 template로 넘김
    return render(request, 'articles/index.html', context)

# 1. CREATE
# 사용자 입력받는 페이지
# def new(request):
#     return render(request, 'articles/new.html')


# new랑 create를 method에 따라 다르게 동작하게 만들기!!
def create(request):
    # CREATE
    if request.method == 'POST': # METHOD에 따라 다르게 동작..
        # 변수
        title = request.POST.get('title') # GET 방식으로 키에서 값 받음
        content = request.POST.get('content')
        # 1 create
        # article = Article()
        # article.title = title
        # article.content = content
        # article.save() # db에 저장됨!!

        # 2 키워드인자로 넣는 방법
        article = Article(title=title, content=content)
        # 저장 전에 유효성 검증 하기
        article.full_clean()
    # 오류 발생하면...
    # full_clean()에서 아무 오류 없을 때
        article.save()

        # 3 리턴값이 있고 바로 저장됨 -> 저장 전에 검증 불가능...(안쓸것임..)
        # Article.objects.create(title=title, content=content)
    
        return redirect(article) # 메인페이지 / article.pk (article에서 detail로 바로 넘어갈 수 있음!!)
        # detail은 저장된 객체 덩어리만 넣어주면 됨!!!
    # NEW
    else:
        return render(request, 'articles/create.html')


# articles/1 => 1번글로 하고싶음
def detail(request, pk):
    
    article = Article.objects.get(pk=pk) # article의 pk = 매개변수 pk
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk) # 선택하고
    # post 일때만 삭제!!
    if request.method == 'POST':
        article.delete() # 삭제
        return redirect('articles:index') # 삭제 성공 후 메인페이지로 돌아가도록 한다.
    # get방식 이면 삭제 안됨!
    else:
        return redirect(article)

# def edit(request, pk): # 뭘수정할지 pk로 받아야함
#     article = Article.objects.get(pk=pk)
#     context = {'article': article,}
#     return render(request, 'articles/edit.html', context)

def update(request, pk): # 몇 번 글을 수정할지 받아야함
    article = Article.objects.get(pk=pk)
    # UPDATE
    if request.method == 'POST':
        article.title = request.POST.get('title') # 기존의 article.title을 바꿔준다!!
        article.content = request.POST.get('content')
        article.save()
        return redirect(article)
    # EDIT
    else:
        context = {'article': article,}
        return render(request, 'articles/update.html', context)