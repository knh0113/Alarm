from django.db import models
from django.conf import settings


class User(models.Model):
    username = models.CharField(max_length=64,verbose_name = '사용자명')
    password = models.CharField(max_length=64,verbose_name = '비밀번호')
    usercollege = models.CharField(max_length=64,verbose_name = '학교')
    
    def __str__(self): # 이 함수 추가
        return self.username  # User object 대신 나타낼 문자 

    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'user_db'

class Like(models.Model):
    like_username = models.ForeignKey('User', on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'likes'

class Follow(models.Model):
    following = models.ForeignKey('User', related_name = "following", on_delete=models.CASCADE)

    class Meta:
        db_table = 'follows'

