from django.db import models

class Lesson(models.Model):
    program_name = models.CharField(max_length=200, verbose_name="프로그램명")
    program_type = models.CharField(max_length=100, verbose_name="유형")
    target = models.CharField(max_length=100, verbose_name="대상")
    duration = models.CharField(max_length=50, verbose_name="시간")
    location = models.CharField(max_length=200, verbose_name="장소")
    purpose = models.TextField(verbose_name="목적")
    preparation = models.TextField(verbose_name="사전 준비물")
    main_contents = models.TextField(verbose_name="주요 내용")
    post_activity = models.TextField(verbose_name="사후 활동")
    classification_criteria = models.CharField(max_length=100, verbose_name="분류 기준")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")

    def __str__(self):
        return self.program_name
