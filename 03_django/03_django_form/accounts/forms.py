from django.contrib.auth.forms import UserChangeForm # 상속받음
from django.contrib.auth import get_user_model

# 회원정보 수정 폼 => email, first_name, last_name 수정.
# 필드 -> user objects 확인 https://docs.djangoproject.com/en/2.2/topics/auth/default/#user-objects
class CustomUserChangeFrom(UserChangeForm):
    class Meta:
        model = get_user_model() # return User (User라는 모델 호출함..)
        fields = ('email', 'first_name', 'last_name',)