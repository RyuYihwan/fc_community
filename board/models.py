from django.db import models


# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE,
                               verbose_name='작성자')
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
    register_dttm = models.DateTimeField(auto_now_add=True,
                                         verbose_name='등록시간')

    # 클래스 문자열로 변환시 유저 네임을 표시하도록 설정
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fc_board'  # 테이블명 지정
        verbose_name = 'fc게시글'
        verbose_name_plural = 'fc게시글 리스트'  # 복수형 이름 지정, 안하면 s 붙여서 표시됨.
