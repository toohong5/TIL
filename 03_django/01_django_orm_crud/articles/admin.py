from django.contrib import admin
from .models import Article # . : 명시적 상대경로 표현

# Register your models here.
class ArticleAdmin(admin.ModelAdmin): # admin.ModelAdmin에서 상속받음
    # 튜플이나 리스트로 작성한다.
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    list_filter = ('created_at',) # 원소 한개일때 끝에 , 안쓰면 튜플 아님!!! # 조건
    list_display_links = ('content',)
    list_editable = ('title',) # 타이틀 수정 가능하게 함
    # 기본값 = 100
    list_per_page = 2 # 한페이지에 2줄씩만 보여줌
admin.site.register(Article, ArticleAdmin)