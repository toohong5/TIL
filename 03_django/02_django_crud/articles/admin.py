from django.contrib import admin
from .models import Article # model에서 Article 가져오기
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)

admin.site.register(Article, ArticleAdmin)

# model에서 잘작성되었는지 확인하기 위해 admin 작성.

