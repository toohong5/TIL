from django.urls import path
from . import views # 현재디렉토리의 view를 연결

app_name = 'articles' # app name 설정해주기!!
urlpatterns = [
    path('', views.index, name='index'), # /article 하면 바로 넘어감.
    # path('new/', views.new, name='new'), # create로 new랑 create 역할 함.
    path('create/', views.create, name='create'), # NEW(GET) + CREATE(POST)
    path('<int:article_pk>/', views.detail, name='detail'), # 특정글로 넘어가게 함
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:article_pk>/update/', views.update, name='update'), # EDIT(GET) + UPDATE(POST)
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'), # DETAIL(GET) + CREATE(POST) -> GET이면 DETAIL보여주고 POST면 댓글 작성
    path('<int:article_pk>/<int:comment_pk>/comments/', views.comments_delete, name='comments_delete'), # DETAIL(GET) + DELETE(POST)
] 