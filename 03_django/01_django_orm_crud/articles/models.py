from django.db import models

# Create your models here.
class Article(models.Model): # models.Model 의 상속을 받는다.
# models.py는 데이터베이스와 파이썬의 중간에 있음
    # id(프라이머리 키) 는 기본적으로 처음 테이블 생성시 자동으로 만들어진다. -> 앞으로 따로 작성하지 않음!
    # id = models.AutoField(primary_key=True) # 번호를 자동으로 입력해줌\
    
    # 클래스 변수들 -> 테이블을 생성해 각 column들(title, content, created_at)을 작성했음
    title = models.CharField(max_length=10) # 글자수 제한하는 문자열필드
    content = models.TextField() # 무한정 들어갈 수 있는 텍스트필드
    created_at = models.DateTimeField(auto_now_add=True) # 최초 일자
    updated_at = models.DateTimeField(auto_now=True) # 최종수정일자가 들어가야함(계속 갱신됨)

    def __str__(self):
        return f'{self.pk}번글 - {self.title} : {self.content}'
