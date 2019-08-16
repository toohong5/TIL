from django.urls import path
from . import views # 자기의 views를 가져옴

urlpatterns = [
    path('index/', views.index),
]
