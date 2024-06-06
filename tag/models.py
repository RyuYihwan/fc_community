from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그명')

    register_dttm = models.DateTimeField(auto_now_add=True,
                                         verbose_name='등록시간')

    # 클래스 문자열로 변환시 유저 네임을 표시하도록 설정
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fc_tag'  # 테이블명 지정
        verbose_name = 'fc태그'
        verbose_name_plural = 'fc태그 리스트'  # 복수형 이름 지정, 안하면 s 붙여서 표시됨.