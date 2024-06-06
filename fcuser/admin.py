from django.contrib import admin
from .models import Fcuser


# from django.contrib.sessions.models import Session

# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(Fcuser, FcuserAdmin)

# 세션 테스트
# admin.site.register(Session)
