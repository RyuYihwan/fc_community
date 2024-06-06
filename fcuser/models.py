from django.db import models


# Create your models here.

class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')
    useremail = models.EmailField(max_length=128,
                                 verbose_name='사용자이메일')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    register_dttm = models.DateTimeField(auto_now_add=True,
                                         verbose_name='등록시간')

    # 클래스 문자열로 변환시 유저 네임을 표시하도록 설정
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'fcuser'  # 테이블명 지정
        verbose_name = 'fc사용자'
        verbose_name_plural = 'fc사용자 리스트' # 복수형 이름 지정, 안하면 s 붙여서 표시됨.

