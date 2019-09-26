from django.contrib import admin
from .models import Article, Comment
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'updated_at', 'article_id',) # 왜래키 -> 'article_id'

admin.site.register(Comment, CommentAdmin)

# 위와 동일한 역할임...
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'content', 'created_at', 'updated_at', 'article_id',)