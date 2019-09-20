from django.urls import reverse
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

    # detail에서만 사용함.
    def get_absolute_url(self):
        # return f'/articles/{self.pk}/'
        # return reverse('articles:detail', args=[self.pk]) # articles/10/
        return reverse('articles:detail', kwargs={'article_pk': self.pk}) # key이름은 view에서 작성한 함수의 매개변수로..
        # 주의사항
        # reverse 함수에 args 랑 kwargs 를 동시에 인자로 보낼 수 없다.

class Comment(models.Model):
    # to의 소문자로 변수명
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # (Article에 연결시킨다, 부모 삭제시 자식도 삭제됨)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True) # 저장되는 순간 알아서 장고가 만들어줌
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:            
        ordering = ['-pk'] # 애초에 모델에서 오더링을 바꿔줌..
    def __str__(self):
        # return self.content
        return f'<Article({self.article_id}): Comment({self.pk})-{self.content}'