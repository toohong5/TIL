from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20) # blank=True 하면 빈값 넣어도 유효성 검증시 패스됨!
    content = models.TextField() # blank=True 하면 빈값 넣어도 검증시 패스됨!
    created_at = models.DateTimeField(auto_now_add=True) # 저장되는 순간 알아서 장고가 만들어줌
    updated_at = models.DateTimeField(auto_now=True)
    
    # 객체표현
    def __str__(self):
        return self.title # 보통 첫번째 칼럼을 해줌