# Generated by Django 3.2.25 on 2024-06-06 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fcuser', '0004_auto_20240606_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fcuser.fcuser', verbose_name='작성자')),
            ],
            options={
                'verbose_name': 'fc게시글',
                'verbose_name_plural': 'fc게시글 리스트',
                'db_table': 'fc_board',
            },
        ),
    ]
