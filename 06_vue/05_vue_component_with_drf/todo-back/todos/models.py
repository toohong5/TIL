from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
# 커스텀한 유저모델 사용
class User(AbstractUser):
    pass

class Todo(models.Model):
    # 1:N 관계
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False) # default 값 설정 필요

    def __str__(self):
        return self.title
