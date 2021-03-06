# 이미지키트 사용
from imagekit.models import ProcessedImageField , ImageSpecField # ProcessedImageField: 썸네일만 올림 / ImageSpecField: 원본으로 부터 썸네일 생성함..
from imagekit.processors import Thumbnail
from django.urls import reverse
from django.db import models

def articles_image_path(instance, filename):
    return f'articles/{instance.pk}/images/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField() 
    image = models.ImageField(blank=True) # 원본이미지
    # 위의 IMAGE로 부터 THUMBNAIL 만들어짐!
    # image_thumbnail = ImageSpecField(
    #     source='image', # 원본 ImageField 이름
    #     processors=[Thumbnail(200, 300)],
    #     format='JPEG',
    #     options={'quality': 90},
    # )
    image = ProcessedImageField(
        # ProcessedImageField 에 인자로 들어가 있는 값들은 migrations 이후에
        # 추가되거나 수정되더라도 makemigrations를 하지 않아도 된다.
        processors=[Thumbnail(200, 300)], # 처리할 작업 목록,(이미지를 200*300으로 잘라서 들어가게 함 )
        format='JPEG', # 저장 포맷
        options={'quality': 90}, # 추가 옵션들
        upload_to='articles/images', # 저장 위치(MEDIA_ROOT/article/images)
    ) # 이미지 경로 문자열로 저장됨! (blank=True 해줘야 빈값도 저장 허용됨.)
    # 중간에 썼지만 맨 나중에 
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