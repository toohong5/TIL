from django.urls import path
from . import views # 현재디렉토리의 view를 연결
urlpatterns = [
    path('', views.index), # /article 하면 바로 넘어감.
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/', views.detail), # 특정글로 넘어가게 함
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update),
]
